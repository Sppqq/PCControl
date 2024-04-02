import psutil


def ext():
    # search all 'python.exe' process
    for proc in psutil.process_iter():
        try:
            if proc.name() == "python.exe":
                proc.terminate()
        except psutil.NoSuchProcess:
            pass


ext()