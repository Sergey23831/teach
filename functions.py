import os
from datetime import datetime

APP_DIR = os.path.dirname(os.path.realpath(__file__))       # НАЗНАЧАЕМ ПАПКУ ПО УМОЛЧАНИЮ

###########################
#  ФУНКЦИЯ ЗАПИСИ В ФАЙЛ  #
###########################
def write_file(name, data):
    try:
        # time = datetime.now()
        # time = time.strftime(" %Y-%m-%d %H:%M:%S")
        # name = name + time
        my_file = open(f"{name}.txt", "a+")                 # ОТКРЫТИЕ ФАЙЛА НА ЗАПИСЬ В РЕЖИМЕ ДОЗАПИСИ
        my_file.write(f"{data}\n")                          # ЗАПИСЬ ДАННЫХ В ФАЙЛ
        my_file.close()                                     # ЗАКРЫТИЕ ФАЙЛА
        return f"file : \"{name}.txt\" write OK"
    except:
        return f"file : \"{name}.txt\" write FAIL"

def get_current_timedate():
    time = datetime.now()
    time = time.strftime(" %Y-%m-%d %H:%M:%S")
    return time
