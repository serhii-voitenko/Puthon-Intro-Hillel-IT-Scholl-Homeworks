"""
1.Написать функцию, которая выведет все пятницы 13-го в указаном году. Использовать можно все что прошли
"""

from datetime import date, timedelta


def friday_13_in_year(y):
    day = date(y, 1, 1)
    end = date(y, 12, 31)
    one_day = timedelta(days=1)
    while day < end:
        if day.weekday() == 4 and day.day == 13:
            yield day
        day += one_day


print([str(d) for d in friday_13_in_year(2019)])


"""
2.Реализовать функции min и max
Функции принимают 1 аргумент (list с числами) и возвращает максимальное/минимальное значение. Использовать сортировку 
нельзя.
"""

oper_list = []


def min_max(num_list):
    global oper_list
    try:
        oper_list = num_list.split()
        oper_list = [int(item) for item in oper_list]
    except ValueError:
        input(f'Yo should write a digits separated by space: ')
    print(f' The smallest number is {min(oper_list)}')
    print(f' The biggest number is {max(oper_list)}')


min_max(input('Enter a list numbers or elements separated by space: '))


"""
3.Написать функцию, которая принимает 1 аргумент — год, и возвращающую True, если год високосный, иначе False
"""


def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(isleap(2020))


"""
4.Написать игру. 2 игрока бросают игровые кубики по 10 раз,

нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).

Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.

(модуль random)
"""

from random import randint

sum1 = 0
sum2 = 0
name1 = str(input("First player name: "))
name2 = str(input("Second player name: "))


def cubes_the_game():
    while True:
        command = input('Enter \'p\' to throw a dice or enter \'q\' to quit the game: ')
        if command == 'p':
            play()
        elif command == 'q':
            print('Return later.')


def play():
    global sum1, sum2
    for throw in range(10):
        val1 = randint(1, 6)
        val2 = randint(1, 6)
        if val1 == val2:
            print('Please repeat: ')
            cubes_the_game()
        else:
            sum1 = sum1 + val1
            sum2 = sum2 + val2
    if sum1 > sum2:
        return print(f'{name1} player WIN with score: {sum1}')
    elif sum1 < sum2:
        return print(f'{name2} player WIN with score: {sum2}')
    else:
        return print('We have a DRAW!')


cubes_the_game()


"""
5.Написать функцию для сортировки для данного списка словарей.

Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`
"""

data = [
    {'name': 'Bill', 'lastname': 'Boll'},
    {'name': 'Bob', 'lastname': 'Zip'},
    {'lastname': 'Fuf'},
    {'lastname': 'Albertus'},
    {'name': 'Dimon', 'lastname': 'Nomid'},
]


def sort_func(i):
    if 'name' in i.keys():
        return i['name']
    else:
        return i['lastname']


data.sort(key=sort_func)
print(data)
