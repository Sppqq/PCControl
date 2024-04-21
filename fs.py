import os

dir_files = os.listdir()

if not 'start.bat' in dir_files:
    with open('start.bat', 'w') as f:
        f.write('@ECHO OFF\n\npython start_tray.py')
if not 'stop.bat' in dir_files:
    with open('stop.bat', 'w') as f:
        f.write('@ECHO OFF\n\ntaskkill /f /im "python.exe"')
if not 'restart.bat' in dir_files:
    with open('restart.bat', 'w') as f:
        f.write('@ECHO OFF\n\nCALL stop.bat\nCALL start.bat')
