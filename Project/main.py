# _____             ______ _ _
# |  __ \           |  ____(_) |
# | |__) |   _ _ __ | |__   _| | ___
# |  _  / | | | '_ \|  __| | | |/ _ \
# | | \ \ |_| | | | | |    | | |  __/
# |_|  \_\__,_|_| |_|_|    |_|_|\___|


import itertools
import threading
import time
import sys
import os
from SixerpAPI import *
from SixerpAPI import Time_API as GET_TIME
from SixerpAPI import Authors_API as GET_AUTHORS
from SixerpAPI import Repeat_API as GET_REPEAT  # Для конца программы.
from SixerpAPI import INFOAPI_API as GET_INFOAPI


class Cars:
    mark = "Не уствновлено"
    weight = 'Не установлен'
    speed = 'Не установлена'
    model = 'Не установлена'
    made_in = 'Не известно'
    issue = 'Не указано'

    def set(self, mark, weight, speed, model, made_in, issue):
       self.mark = mark
       self.weight = weight
       self.speed = speed
       self.model = model
       self.made_in = made_in
       self.issue = issue


class Moto(Cars):
    wheels = 2


print()
done = False


# Сама анимация
def animation():
    for c in itertools.cycle(['|', '/', '-', '\\']):
       if done:
          break
       sys.stdout.write('\rЗагрузка файлов' + c)
       sys.stdout.flush()
       time.sleep(0.1)
    sys.stdout.write('\rФайлы загружены! ')


t = threading.Thread(target=animation)
t.start()

# Длинный процесс
time.sleep(3)
done = True
time.sleep(1)
print()

# Дата, время, авторы импортируются из API
GET_TIME()
GET_AUTHORS()

# Начало программы,
# Регестрация

print('\nЗдравствуйте! \n Добро пожаловать в наш виртуальный автосалон.')
# f = open('logins.txt', "w")
USER_LOGIN = (input('Чтобы продолжить работу, зарегестрируйтесь, введя Ваш логин: '))
time.sleep(1)
print('Успешно!')
USER_PASSWORD = (input('Теперпь, введите Ваш пароль: '))
time.sleep(1)

print()

print('Загрузка.')
time.sleep(2)
print('Загрузка..')
time.sleep(0.5)
print('Загрузка...')

print('##############################')
print('Ваши данные успешно были занесены в Базу Данных [Login is: ' + USER_LOGIN + ', Password is: ' + str(
    USER_PASSWORD) + ']')
UniqueID_API()
print('##############################')
time.sleep(5)
print()
print()
print(
    "В нашем автосалоне имеются: Автомобили🚗 и Мотоциклы, скажите, что Вы хотите просмотреть, введя 1 или 2, где 1 - Авто, 2 - Мото ")  # 🚗
CHOICE = input('Я хочу просмотреть: ')

if CHOICE == '1':
    print('Вы выбрали просмотр автомобилей')
    time.sleep(1)
    print('Автомобили:')
    print('Germany: \n --Mercedes \n --BMW \n --Audi \n --Volkswagen')
    print('---')
    print("Japan: \n --Nissan \n --Mitsubishi \n --Toyota \n --LEXSUS ")

    print('Желаете просмотреть какой-либо автомобиль более детально?')
    print('Да/Нет' + Registerwords_API())
    CARS_USER_ANSWER = input('-> ')

    if CARS_USER_ANSWER == 'Да' or 'Yes':
       print('Какой страны марку машины Вы хотите просмотреть?')
       print('Germany/Japan' + Registerwords_API())
    CARS_USER_ANSWER1 = input('-> ')
    if CARS_USER_ANSWER1 == 'Germany':
       print('Вы выбрали GERMANY:')
       time.sleep(1)
       print('Какую марку машины вы хотите просмотреть? ')
       CAR_CHOICE = input('-> ')
       if CAR_CHOICE == 'Mercedes':
          Mercedes = Cars()
          Mercedes.set('Mercedes', '1Т650КГ', 140, 'CLK', 'GERMANY', '2007')
          print('Марка: ' + Mercedes.mark)
          print('Вес: ' + Mercedes.weight)
          print('Скорость: ' + str(Mercedes.speed))
          print('Модель: ' + Mercedes.model)
          print('Страна производетель: ' + Mercedes.made_in)
          print('Год выпуска: ' + Mercedes.issue)
       if CAR_CHOICE == 'BMW':
          BMW = Cars()
          BMW.set('BMW', '1Т900КГ', 190, 'M-CLASS', 'GERMANY', '2015')
          print('Марка: ' + BMW.mark)
          print('Вес: ' + BMW.weight)
          print('Скорость: ' + str(BMW.speed))
          print('Модель: ' + BMW.model)
          print('Страна производетель: ' + BMW.made_in)
          print('Год выпуска: ' + BMW.issue)
       if CAR_CHOICE == 'Audi':
          Audi = Cars()
          Audi.set('Audi', '2Т', 180, 'A-CLASS', 'GERMANY', '2014')
          print('Марка: ' + Audi.mark)
          print('Вес: ' + Audi.weight)
          print('Скорость: ' + str(Audi.speed))
          print('Модель: ' + Audi.model)
          print('Страна производетель: ' + Audi.made_in)
          print('Год выпуска: ' + Audi.issue)
       if CAR_CHOICE == 'Volkswagen':
          Volkswagen = Cars()
          Volkswagen.set('Volkswagen', '1Т950КГ', 165, 'TIGUAN', 'GERMANY', '2017')
          print('Марка: ' + Volkswagen.mark)
          print('Вес: ' + Volkswagen.weight)
          print('Скорость: ' + str(Volkswagen.speed))
          print('Модель: ' + Volkswagen.model)
          print('Страна производетель: ' + Volkswagen.made_in)
          print('Год выпуска: ' + Volkswagen.issue)

    elif CARS_USER_ANSWER1 == 'Japan':
       print('Вы выбрали JAPAN:')
       time.sleep(1)
       print('Какую марку машины вы хотите просмотреть? ')
       CAR_CHOICE = input('-> ')
       if CAR_CHOICE == 'Nissan':
          Nissan = Cars()
          Nissan.set('Nissan', '2Т300', 165, 'PATROL', 'JAPAN', '2018')
          print('Марка: ' + Nissan.mark)
          print('Вес: ' + Nissan.weight)
          print('Скорость: ' + str(Nissan.speed))
          print('Модель: ' + Nissan.model)
          print('Страна производетель: ' + Nissan.made_in)
          print('Год выпуска: ' + Nissan.issue)
       if CAR_CHOICE == 'Mitsubishi':
          Mitsubishi = Cars()
          Mitsubishi.set('Mitsubishi', '2Т500КГ', 170, 'PAJERO', 'JAPAN', '2014')
          print('Марка: ' + Mitsubishi.mark)
          print('Вес: ' + Mitsubishi.weight)
          print('Скорость: ' + str(Mitsubishi.speed))
          print('Модель: ' + Mitsubishi.model)
          print('Страна производетель: ' + Mitsubishi.made_in)
          print('Год выпуска: ' + Mitsubishi.issue)
       if CAR_CHOICE == 'Toyota':
          Toyota = Cars()
          Toyota.set('Toyota', '2Т', 185, 'KAMRI V40', 'JAPAN', '2012')
          print('Марка: ' + Toyota.mark)
          print('Вес: ' + Toyota.weight)
          print('Скорость: ' + str(Toyota.speed))
          print('Модель: ' + Toyota.model)
          print('Страна производетель: ' + Toyota.made_in)
          print('Год выпуска: ' + Toyota.issue)
       if CAR_CHOICE == 'LEXSUS':
          LEXSUS = Cars()
          LEXSUS.set('LEXSUS', '2Т700КГ', 165, 'LX 570', 'JAPAN', '2015')
          print('Марка: ' + LEXSUS.mark)
          print('Вес: ' + LEXSUS.weight)
          print('Скорость: ' + str(LEXSUS.speed))
          print('Модель: ' + LEXSUS.model)
          print('Страна производетель: ' + LEXSUS.made_in)
          print('Год выпуска: ' + LEXSUS.issue)

    Cars()
    if CARS_USER_ANSWER == 'Нет' or 'No':
        print('')
        exit(0)
        sys.exit
        os.abort()

if CHOICE == '2':
    print('Мотоциклы:')
    print('Germany: \n --Не установлено')
    print('---')
    print("Japan: \n --Не установлено")

    print('Желаете просмотреть какой-либо мотоцикл более детально?')
    print('Да/Нет' + Registerwords_API())
    MOTO_USER_ANSWER = input('-> ')

    if MOTO_USER_ANSWER == 'Да':
       print('Какой страны марку мотоцикла Вы хотите просмотреть?')
       print('Germany/Japan' + Registerwords_API())
    MOTO_USER_ANSWER1 = input('-> ')
    if MOTO_USER_ANSWER1 == 'Germany':
       print(HASNOT_API())
    elif MOTO_USER_ANSWER1 == 'Japan':
       print(HASNOT_API())
    else:
        print("Такого раздела нет!")

# if WANT == 'Mercedes':
#     Mercedes = Cars()
#     Mercedes.set('Mercedes', '1Т650КГ', 140, 'CLK', 'GERMANY', '2007')
#     print('Марка: ' + Mercedes.mark)
#     print('Вес: ' + Mercedes.weight)
#     print('Скорость: ' + str(Mercedes.speed))
#     print('Модель: ' + Mercedes.model)
#     print('Страна производетель: ' + Mercedes.made_in)
#     print('Год выпуска: ' + Mercedes.issue)

# else:
#     Another = Cars()
#     print('Марка: ' + Another.mark)
#     print('Вес: ' + Another.weight)
#     print('Скорость: ' + Another.speed)
#     print('Модель: ' + Another.model)
#     print('Страна производетель: ' + Another.made_in)
#     print('Год выпуска: ' + Another.issue)
time.sleep(10)
Repeat_API()
INFOAPI_API()
