# Задание 1 **************************************************************
from sys import argv

scr_name, hours_works, temp_hour, bonus = argv

print("Имя скрипта: ", scr_name)
print("Расчет заработной платы сотрудника")
print("Выработка в часах: ", hours_works)
print("Ставка в час: ", temp_hour)
print("Премия: ", bonus)
print("Зарплата сотрудника: ", (float(hours_works) * float(temp_hour)) + float(bonus))

# Задание 2 **************************************************************
print('12 случайных чисел от 1 до 99: ')
print(list)


def max_ascendent_values_in_list(input_list: list):
    output_list = []
    for key, value in enumerate(input_list):
        if key + 1 < len(input_list) and value < input_list[key + 1]:
            output_list.append(input_list[key + 1])

    return output_list


print('Числа из исходного списка, значения которых больше предыдущего элемента: ')
print(max_ascendent_values_in_list(list))

# Задание 3 **************************************************************
print(f'из чисел 20-241, кратные 20 и 21:{[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]}')

# Задание 4 **************************************************************
from random import randint

my_lst = [randint(-10, 10) for _ in range(20)]

print('Исходный список чисел: ')
print(my_lst)

my_dict = {i: 0 for i in my_lst}

for i in my_lst:
    my_dict[i] += 1

print('Уникальные числа из списка:')
print([i for i in my_dict if my_dict[i] == 1])

# Задание 5 **************************************************************
from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание 6 **************************************************************
from itertools import count, \
    cycle

limit = 10
cnt = 0
for el in count(int(input('Введите стартовое число '))):
    cnt += 1
    print(el)
    if cnt >= limit:
        cnt = 0
        break

my_lst = [5, 0, 6, 0]

print('_____________')
for el in cycle(my_lst):
    cnt += 1
    print(el)
    if cnt >= limit:
        cnt = 0
        break

# Задание 7 **************************************************************
from math import factorial


def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(15):
    print(el)
