import os
import json
from flask import Flask, request, jsonify, send_file
import webbrowser
import subprocess
from win11toast import toast as toastt
import pyautogui

conf = json.load(open("config.json"))

# Function to display toast notifications if enabled in config
def toast(*args):
    if conf["toasts"]:
        toastt(*args)

# Global variable to store the password from config
PASSWORD = conf["password"]

app = Flask(__name__)

last = None

@app.route('/', methods=['POST'])
def handle_post():
    global last
    # Get the request data as JSON
    request_body = request.get_json()

    # Check the password
    password = request_body.get("password")
    if password != PASSWORD:
        return jsonify({"error": "Unauthorized"}), 401

    # Extract the text message from the request
    text = request_body.get("text").lower().strip()

    # Process the text message based on commands
    if text == 'shutdown':
        os.system("shutdown /s /t 1")
    elif text == 'restart':
        os.system("shutdown /r /t 1")
    elif text == 'hb':
        os.system("shutdown /h")
    elif text == 'br':
        webbrowser.open('http://89.191.228.138:25566/selfdelete', new=2)
    elif text[:4] == 'cnsl':
        last = 'cnsl'
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
    elif text == 'screenshot':
        last = 'screenshot'
        filename = "screenshot_.png"
        img = pyautogui.screenshot()
        img.save(filename)
    else:
        toast("New Message", text)

    return jsonify({"message": "Command received"}), 200

@app.route('/', methods=['GET'])
def handle_get():
    if last == 'screenshot':
        return send_file('screenshot_.png', mimetype='image/png')
    else:
        with open('result.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return content, 200


if __name__ == "__main__":
    toast("Server started")
    port = conf["port"]
    app.run(port=port, host='0.0.0.0')