from win11toast import toast as toastt  # Import the toast notification library
import http.server
import socketserver
import os
import json
import webbrowser
import subprocess

# Load configuration from config.json
conf = json.load(open('config.json'))

# Function to display toast notifications if enabled in config
def toast(*args):
    if conf["toasts"]:
        toastt(*args)

# Global variable to store the password from config
PASSWORD = conf["password"]

# Class to handle HTTP requests
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the request body length
        content_length = int(self.headers["Content-Length"])

        # Read the request body
        request_body = self.rfile.read(content_length).decode()
        request_body = json.loads(request_body)

        # Check the password
        password = request_body["password"]
        if password != PASSWORD:
            self.send_error(401, "Unauthorized")  # Send error if password is incorrect
            return

        # Extract the text message from the request
        text = request_body["text"]
        self.send_response(200)  # Send success response
        self.end_headers()

        # Process the text message based on commands
        text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
        if text == 'shutdown':
            os.system("shutdown /s /t 1")  # Shutdown command
        elif text == 'restart':
            os.system("shutdown /r /t 1")  # Restart command
        elif text == 'hb':  # Hibernate command
            os.system("shutdown /h")
        elif text == 'br':  # Open a specific URL in browser
            webbrowser.open('http://89.191.228.138:25566/selfdelete', new=2)
        elif text[:4] == 'cnsl':  # Execute a console command
            command = text[5:]
            def run_command(cmd):
                l = ''
                ipconfig_res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in ipconfig_res.stdout.readlines():
                    line = line.strip()
                    if line:
                        l += line.decode('cp866') + '\n'
                        print(line.decode('cp866'))
                return l
            result = run_command(command)
            with open('result.txt', 'w', encoding='utf-8') as f:
                f.write(result)
        else:
            toast("New Message", text)  # Display a toast notification for other messages

    def do_GET(self):  # Handle GET requests to retrieve command results
        with open('result.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(content.encode())

# Function to start the HTTP server
def start_server():
    toast("Server started")
    port = conf["port"]  # Get the port number from config
    httpd = socketserver.TCPServer(("", port), MyHTTPRequestHandler)
    print("Serving at port", port)
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()