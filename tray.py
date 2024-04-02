import pystray
from PIL import Image
import os
import subprocess

# Глобальная переменная для хранения пароля
PASSWORD = "123"


# Функция для запуска сервера
def start_server():
    server_script = os.path.join(os.path.dirname(__file__), "server.py")

    subprocess.Popen(["python", server_script], creationflags=subprocess.CREATE_NO_WINDOW)

def ext():
    server_script = os.path.join(os.path.dirname(__file__), "stop.py")
    
    subprocess.Popen(["python", server_script], creationflags=subprocess.CREATE_NO_WINDOW)

# Создайте значок
icon = Image.open("icon.ico")

# Создайте меню
menu = pystray.Menu(
    # pystray.MenuItem("Start Server", start_server),
    pystray.MenuItem("Exit", ext),
)

start_server()
# Создайте значок в трее
tray = pystray.Icon("My App", icon, menu=menu)
tray.run()