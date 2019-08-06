 #   _____ _                                   _ 
 #  / ____(_)                      /\         (_)
 # | (___  ___  _____ _ __ _ __   /  \   _ __  _ 
 #  \___ \| \ \/ / _ \ '__| '_ \ / /\ \ | '_ \| |
 #  ____) | |>  <  __/ |  | |_) / ____ \| |_) | |
 # |_____/|_/_/\_\___|_|  | .__/_/    \_\ .__/|_|
 #                        | |           | |      
 #                        |_|           |_|      



# API by SixerpMine [iSixerp]

import datetime
import time
import random

__author__ = 'The group SixerpMine (SAB): which includes Sixerp and Blos '
PVersion = 'The program version is 1.0'

"""""""""
a = datetime.datetime.today().strftime("%Y%m%d")
print(a)  # '20170405'
print(today.strftime("%m/%d/%Y"))  # '04/05/2017'
today = datetime.datetime.today()
"""""""""""

today = datetime.datetime.today()


# print(today.strftime("%d-%m-%Y // %H:%M:%S"))  # 2017-04-05-00.18.00

def ApiVersion():
    print('Версия API: 1.0.1')

def Time_API():
    print('##############################')
    print('Дата и время ' + (today.strftime("%d-%m-%Y // %H:%M:%S")))
    pass

def UniqueID_API():
    PLAYERID = random.randint(20000, 800000000)
    print('Ваш уникальный ID: ' + str(PLAYERID))
    pass

def DefaultAge_API():
    try:
        b = int(input('Возраст? '))
    except ValueError:
        print('Вы ввели не число!')
        print('Установлен дефаултный возраст: 14')
        b = 14
    # print(b)
    pass

def Authors_API():
    print('\n', __author__, '\n', PVersion)
    print('##############################')
    pass


def Repeat_API():
    return Authors_API()


def Registerwords_API():
    RegWord = '\n -> (Регистр учитывается!) <-'
    return RegWord


def HASNOT_API():
    HASNT = 'В настоящий момент, просмотр этого раздела недоступен'
    return HASNT

def INFOAPI_API():
    time.sleep(2)
    print('####################################################')
    print("   _____ _                                   _")
    print("  / ____(_)                      /\         (_)")
    print(" | (___  ___  _____ _ __ _ __   /  \   _ __  _ ")
    print("  \___ \| \ \/ / _ \ '__| '_ \ / /\ \ | '_ \| |")
    print("  ____) | |>  <  __/ |  | |_) / ____ \| |_) | |")
    print(" |_____/|_/_/\_\___|_|  | .__/_/    \_\ .__/|_|")
    print("                        | |           | |")
    print("                        |_|           |_|")
    print('####################################################')
    print()
    print()
    print('ИНФОРМАЦИЯ!')
    print('Главный файл MAIN.py написан благодаря API.')
    ApiVersion()
    print('Создатель API: Sergey Sixerp. \nДля редактирования иных файлов, просьба обращаться к: https://vk.com/sixerpm или https://vk.com/sixerpmine ')
    time.sleep(2)
    quit(0)
    pass

