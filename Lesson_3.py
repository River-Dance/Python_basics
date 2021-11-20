# ЗАДАНИЕ 1 ***************************************************************************************
def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! На ноль делить нельзя')

print(calculator(int(input('Что делим: ')), int(input('На что делим: '))))

# ЗАДАНИЕ 2 ***************************************************************************************
def person(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')

person(
    name=input("Имя: "),
    lastname=input("Фамилия: "),
    year_of_birth=input("Год Рождения: "),
    city=input("Город проживания: "),
    email=input("email: "),
    phone=input("phone: "),
)

# ЗАДАНИЕ 3 ***************************************************************************************
def my_func(arg1, arg2, arg3):
 print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(
 int(input('Аргумент 1:')),
 int(input('Аргумент 2:')),
 int(input('Аргумент 3:')),
)
# ЗАДАНИЕ 4 ***************************************************************************************
def my_func(x, y):
    return x ** y

def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result

print(f'Реализация возведения степени вариантом 1: '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

print(f'Реализация возведения степени вариантом 2: '
      f'{my_func_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

# ЗАДАНИЕ 5 ***************************************************************************************
def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += int(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел, или букву для выхода: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_flag:
        break

# ЗАДАНИЕ 6 ***************************************************************************************
def int_func(word):
   latin_ch = 'qwertyuiopasdfghjklzxcvbnm'
   return word.title() if not set(word).difference(latin_ch) else False

words = input('введите строку из слов разделенных пробелом: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), "")
