# Задание 1 *************************************************************************
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '05-12-2021'
date2 = Date.from_string(d)
is_date = Date.is_date_valid(d)


# Задание 2 *************************************************************************
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите делимое: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())

# Задание 3 *************************************************************************
class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'Всё верно, добавляем "{user_val}" в список. Продолжаем ввод? y/n: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Это не число! Продолжаем ввод? y/n: ").lower()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()


# Задание 4, 5, 6 *************************************************************************
class OfficeEquipmentWarehouse:
    """Класс, описывающий склад оргтехники"""
    print("\nСклад оргтехники")


class OfficeEquipment:
    """Базовый класс оргтехники"""
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    """Класс принтер"""
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"<<Сканер>>"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tтип сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.producer, self.color, self.xer_wi_fi)


p = Printer('Canon', 'white', 'струйный')
p2 = Printer('Brother', 'blue', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())


s = Scanner('Epson', 'black', 'CIS')
s2 = Scanner('Avision', 'white', 'CCD')
s3 = Scanner('Kodak', 'yellow', 'CMOS')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())


x = Xerox('Hanp', 'white', 'есть')
x2 = Xerox('Phaser', 'black', 'есть')
x3 = Xerox('Xerox', 'white', 'есть')
x4 = Xerox('Pantum', 'red', 'отсутствует')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())


# Задание 7 *************************************************************************
class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x1 = x
        self.x2 = y

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'x = {self.x1 + other.x1} + {self.x2 + other.x2} * i'

    def __mul__(self, other):
        print(f'Умножение комплексных чисел')
        return f'x = {self.x1 * other.x1 - (self.x2 * other.x2)} + {self.x2 * other.x1} * i'

    def __str__(self):
        return f'x = {self.x1} + {self.x2} * i'


x1 = ComplexNumber(1, -2)
x2 = ComplexNumber(3, 4)
print(x1 + x2)
print(x1 * x2)