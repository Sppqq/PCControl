import subprocess
import os

# Путь к файлу server.py
server_script = os.path.join(os.path.dirname(__file__), "tray.py")

# Запустите сервер в фоновом режиме
subprocess.Popen(["python", server_script], creationflags=subprocess.CREATE_NO_WINDOW)

# Добавьте код для создания значка в трее и управления сервером
# (как в предыдущем примере с pystray)