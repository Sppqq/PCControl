import subprocess
import json
import os

if os.path.exists('config.json'):
    conf = json.load(open('config.json'))
else:
    conf = {}
    conf["firststart"] = True
    conf["password"] = "123"
    conf["port"] = 10000
    with open('config.json', 'w') as f:
        json.dump(conf, f)
    subprocess.call(['python', 'fs.py'])
    os.remove('fs.py')

    g = input("Have you installed the libraries from requirements.txt? If not, write 'n' and they will be installed (y/n)\n")

    conf = json.load(open('config.json'))
    if g == 'n':
        subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

    os.remove('requirements.txt')

if conf["firststart"]:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    conf["lip"] = s.getsockname()[0]
    with open('config.json', 'w') as f:
        json.dump(conf, f)
    s.close()
    from colorama import Fore
    print(f'{Fore.YELLOW}First start. Do you want to configure config?{Fore.RESET} (y/n)')
    if input() == 'y':
        conf["firststart"] = False
        print(f'{Fore.CYAN}Do you want to change your password? Default 123{Fore.RESET} (y/n)')
        if input() == 'y':
            conf["password"] = input()
        with open('config.json', 'w') as f:
            json.dump(conf, f)
        print(f'{Fore.CYAN}Do you want to change the server port? Default 10000{Fore.RESET} (y/n)')
        if input() == 'y':
            conf["port"] = int(input())
            with open('config.json', 'w') as f:
                json.dump(conf, f)
        print(f'{Fore.CYAN}Do you want to enable toasts?{Fore.RESET} (y/n)')
        if input() == 'y':
            conf["toasts"] = True
            with open('config.json', 'w') as f:
                json.dump(conf, f)
        print(f'{Fore.CYAN}Do you want to add a server to startup?{Fore.RESET} (y/n)')
        if input() == 'y':
            from winreg import *
            from os import path
            PathFile = path.abspath(__file__)
            def Startup():
                StartupKey = OpenKey(HKEY_CURRENT_USER,
                                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                                0, KEY_ALL_ACCESS)
                SetValueEx(StartupKey, 'name', 0, REG_SZ, PathFile)
                CloseKey(StartupKey)
            Startup()
        print(f'{Fore.CYAN}Print yout local ip for apple shortcut{Fore.RESET} (y/n)')
        if input() == 'y':
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            s.close()
            print(f'{Fore.GREEN}Add apple shortcut on your phone from github to control PC{Fore.RESET}')
        print(f'{Fore.GREEN}Done!{Fore.RESET}')
        input('Press enter to start server in tray')
# Путь к файлу server.py
server_script = os.path.join(os.path.dirname(__file__), "tray.py")

# Запустите сервер в фоновом режиме
subprocess.Popen(["python", server_script], creationflags=subprocess.CREATE_NO_WINDOW)
