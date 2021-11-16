# Задание 1 *************************************************************************
print("Введите число a =")
a = int(input())

print("Введите число b =")
b = int(input())

print("Выберете операцию:")
print("1- сложить a+b")
print("2- вычесть a-b")
print("3- умножить a*b")
print("4- разделить a/b")
d = float(input())

if d==1:
    print("Сумма: a+b =", a+b)

if d==2:
    print("Разность: a-b =", a-b)

if d==3:
    print("Умножение: a*b =", a*b)

if d==4:
    print("Деление: a/b =", a/b)

# Задание 2 *******************************************************************************
time = int(input("Введите время в секудах от 0 до 86 400: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"Время в формате чч:мм:сс - {hours:02}:{minutes:02}:{seconds:02}")

# Задание 3********************************************************************
n = input("Введите целое число, больше 0: ")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n+n) + int(n+n+n)}")

# Задание 4*********************************************************************
num_vvedenoe = int(input("Введите целое, положительное число: "))
peremen_max = 0
num = num_vvedenoe

while num > 0:
    digit = num % 10
    if digit > peremen_max:
        peremen_max = digit
    num = num // 10
print(f"Наибольшей цифрой в числе {num_vvedenoe}, является цифра {peremen_max}")

# Задание 5 *******************************************************************************
income = float(input("Введите выручку компании: "))
expenses = float(input("Введите расходы компании: "))
result = income - expenses

if result > 0:
    print(f"Компания отработала с прибылью {result:.2f} руб")
    print(f"Рентабельность компании {100 * result / income:.1f} %")
    n_person = int(input("Сколько сотрудников в компании? "))
    print(f"Если вы разделите прибыль компании между сотрудниками, то каждый получит по - {result / n_person:.2f} руб")
elif result < 0:
    print(f"Компания отработала в убыток {result:.2f} руб")
else:
    print("Ноль прибыли, лучше чем убыток.")

# Задание 6 *********************************************************************************
while True:
    start_km = float(input("Ваш начальный результат: "))
    finish_km = float(input("Желаемый финишный результат: "))
    deys = 1
    if start_km <= 0 or finish_km < 0:
        print("Результат должен быть больше 0! Стартовое значение должно быть больше 0!")
    else:
        while start_km <= finish_km:
            if start_km == finish_km:
                break
            start_km += start_km / 10
            deys += 1
            print(f"Вы добъетесь результата за {deys} дней")
            break
