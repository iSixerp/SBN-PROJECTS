# d = {
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friday',
#     6: 'Saturday',
#     7: 'Sunday'
# }
# while True:
#     try:
#         i = int(input('Номер дня недели: '))
#     except ValueError:
#         print('Вы ввели не число!')
#     else:
#         print(d.get(i, 'Такого дня нет!'))


a = 15

def DefaultAge_API():
    try:
        b = int(input('Возраст? '))
    except ValueError:
        print('Вы ввели не число!')
        print('Установлен дефаултный возраст: 14')
        b = 14
    print(b)
    pass