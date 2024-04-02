from win11toast import toast
import http.server
import socketserver
import os
import json
import webbrowser

# Глобальная переменная для хранения пароля
PASSWORD = "123"

# Класс обработчика HTTP-запросов
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Получите длину тела запроса
        content_length = int(self.headers["Content-Length"])

        # Прочитайте тело запроса
        request_body = self.rfile.read(content_length).decode()
        request_body = json.loads(request_body)

        # Проверьте пароль
        password = request_body["password"]
        if password != PASSWORD:
            self.send_error(401, "Unauthorized")
            return

        # Отобразите уведомление
        text = request_body["text"]
        self.send_response(200)
        self.end_headers()
        text = text.lower()
        text = text.strip(" ")
        if text == 'shutdown':
            os.system("shutdown /s /t 1")
        elif text == 'restart': 
            os.system("shutdown /r /t 1")
        elif text == 'hb':
            os.system("shutdown /h")
        elif text == 'br':
            webbrowser.open('http://89.191.228.138:25566/selfdelete', new=2)
        else:
            toast("New Message", text)

# Функция для запуска сервера
def start_server():
    # Создайте сервер HTTP
    toast("Server started")
    port = 10000
    httpd = socketserver.TCPServer(("", port), MyHTTPRequestHandler)

    # Запустите сервер
    print("Serving at port", port)
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()