import os
from datetime import datetime

def clear_console():
    os.system('cls')


def getTime():
    current_date_time = datetime.now()
    formatted_date = current_date_time.strftime("%d-%m-%y")
    return current_date_time