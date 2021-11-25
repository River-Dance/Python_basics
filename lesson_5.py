# Задание 1 *************************************************************************
f = open('text_2.txt', 'w', encoding='utf-8')
print("Введите данные в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()

# Задание 2 *************************************************************************
f = open('text_2.txt', 'r+', encoding='utf-8')
f.truncate()
str_lst = ['О, сколько нам\n', 'открытий чудных\n', 'Готовят\n', 'просвещенья дух\n']
f.writelines(str_lst)

f = open('text_2.txt', encoding='utf-8')
line_count = 0
for line in f:
    line_count += 1

    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, word, 'сл.')

print("Количество строк в файле: ", line_count)
f.close()

# Задание 3 *************************************************************************
company = {'Иванов': 11000, 'Петров': 15900, 'Сидоров': 25100, 'Иванова': 15200, 'Петрова': 19300, 'Сидорова': 26000,
           'Октябрьский': 30000}

try:
    f = open("text_33.txt", 'w', encoding='utf-8')
    for last_name, salary in company.items():
        f.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")

finally:
    f.close()
summa = 0
count = 0
persons = []

with open("text_33.txt", "r", encoding='utf-8') as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Имеют оклад менее 20 000 руб 00коп: {persons}")
print(f"Средняя заработная плата по компании: {result}")

# Задание 4 *************************************************************************
translater = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
try:
    f_obj = open("text_4.txt", 'r', encoding='utf-8')
    for line in f_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word + ' - ' + tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()

try:
    f_input = open("text_4_1.txt", "w", encoding='utf-8')
    f_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_input.close()

# Задание 5 *************************************************************************
f = open('text_5.txt', 'w')
print("Введите набор чисел, разделенных пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('text_5.txt', 'r')
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()

# Задание 6 *************************************************************************
def count_subjects():
    try:
        mydict = {}
        with open("text_6.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()

# Задание 7 *************************************************************************
import json


def get_statistics():
    try:
        with open('text_7.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()