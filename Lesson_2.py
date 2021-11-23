# ЗАДАНИЕ 1 ***************************************************************************************
my_int = 5
my_float = 1, 2
my_str = "Привет, мир"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'город': 'Кемерово', 'страна': 'Россия'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

# ЗАДАНИЕ 2 ***************************************************************************************
my_list = input("Введите элементы списка через пробел: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)

# ЗАДАНИЕ 3 Вариант 1 ***************************************************************************************
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц по номеру "))
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

# ЗАДАНИЕ 3 Вариант 2***************************************************************************************
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Введите число месяца в году (от 1 до 12): '))
for period in seasons.keys():
    if month in seasons[period]:
        print(f"По числу месяца - {month}, соответствует периоду года - {period}")

# ЗАДАНИЕ 4 ***************************************************************************************
my_string = input("введите предложение ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word[element]}")
        number += 1
    else:
        print(f" {number} {my_word[element][0:10]}")
        number += 1

# ЗАДАНИЕ 5 ***************************************************************************************
ratings = [5, 4, 3, 2, 1]
print(f"Рейтинг - {ratings}")

while True:
    rating = input('Введите новое значение рейтинга: ')
    try:
        rating = abs(int(rating))
    except ValueError as e:
        print('Ошибка ввода')
        continue

    if not ratings.count(rating):
        if rating > ratings[0]:
            ratings.insert(0, rating)
        elif rating < ratings[-1]:
            ratings.append(rating)
        else:
            for k, v in enumerate(ratings):
                if rating > v:
                    ratings.insert(k, rating)
                    break
    else:
        new_index = ratings.index(rating) + ratings.count(rating)
        ratings.insert(new_index, rating)

    print(ratings)

# ЗАДАНИЕ 6 ***************************************************************************************
inventory_tuple_list = []
i = 1
while True:
 inventory_tuple_list.append(
  (input('Введите номер товара: '), dict({
   'название': str(input('Введите название: ')),
   'цена': float(input('Введите цену: ')),
   'количество': int(input('Введите количество: ')),
   'eд': str(input('Введите единцы измерения: ')),
  }))
 )

 if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
  break

 i += 1

print(f'список товаров:{inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
 for key, value in product[-1].items():
  if key in output_dict:
   if value not in output_dict.get(key):
    output_dict.get(key).append(value)
  else:
   output_dict.update({key: [value]})

print(f'собрана аналитика: {output_dict}')