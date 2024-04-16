from win11toast import toast as toastt
import http.server
import socketserver
import os
import json
import webbrowser
import subprocess
conf = json.load(open('config.json'))
def toast(*args):
    if conf["toasts"]:
        toastt(*args)

# Глобальная переменная для хранения пароля
PASSWORD = conf["password"]

def convert_cr866_to_utf8(input_text):
    """
    Converts CR866 (CP866) encoded text to UTF-8.
    
    Args:
        input_text (str): The input text in CR866 encoding.
        
    Returns:
        str: The converted text in UTF-8 encoding.
    """
    # Define the CR866 to UTF-8 mapping
    cr866_to_utf8 = {
        '\u0410': 'А', '\u0411': 'Б', '\u0412': 'В', '\u0413': 'Г',
        '\u0414': 'Д', '\u0415': 'Е', '\u0416': 'Ж', '\u0417': 'З',
        '\u0418': 'И', '\u0419': 'Й', '\u041A': 'К', '\u041B': 'Л',
        '\u041C': 'М', '\u041D': 'Н', '\u041E': 'О', '\u041F': 'П',
        '\u0420': 'Р', '\u0421': 'С', '\u0422': 'Т', '\u0423': 'У',
        '\u0424': 'Ф', '\u0425': 'Х', '\u0426': 'Ц', '\u0427': 'Ч',
        '\u0428': 'Ш', '\u0429': 'Щ', '\u042A': 'Ъ', '\u042B': 'Ы',
        '\u042C': 'Ь', '\u042D': 'Э', '\u042E': 'Ю', '\u042F': 'Я',
        '\u0430': 'а', '\u0431': 'б', '\u0432': 'в', '\u0433': 'г',
        '\u0434': 'д', '\u0435': 'е', '\u0436': 'ж', '\u0437': 'з',
        '\u0438': 'и', '\u0439': 'й', '\u043A': 'к', '\u043B': 'л',
        '\u043C': 'м', '\u043D': 'н', '\u043E': 'о', '\u043F': 'п',
        '\u0440': 'р', '\u0441': 'с', '\u0442': 'т', '\u0443': 'у',
        '\u0444': 'ф', '\u0445': 'х', '\u0446': 'ц', '\u0447': 'ч',
        '\u0448': 'ш', '\u0449': 'щ', '\u044A': 'ъ', '\u044B': 'ы',
        '\u044C': 'ь', '\u044D': 'э', '\u044E': 'ю', '\u044F': 'я'
    }
    
    # Convert the input text using the mapping
    output_text = ''.join(cr866_to_utf8.get(char, char) for char in input_text)
    return output_text


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
    port = conf["port"]
    httpd = socketserver.TCPServer(("", port), MyHTTPRequestHandler)

    # Запустите сервер
    print("Serving at port", port)
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()