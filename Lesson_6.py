# Задание 1 *************************************************************************
import time
import itertools


class TrafficLights:
    __color = [['RED', [7, "\033[0;31m"]], ['YELLOW', [2, '\033[0;33m']], ['GREEN', [2, "\033[0;32m"]],
               ['YELLOW', [2, '\033[0;33m']]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033{light[1][1]}\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


traffic_ligh_1 = TrafficLights()
traffic_ligh_1.running()


# Задание 2 *************************************************************************
class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()


# Задание 3 *************************************************************************
class Worker:
    name = "Петр"
    surname = "Петров"
    position = "Конструктор"
    profit = 25000
    bonus = 5000
    _income = {"Оклад": profit,
               "Премия": bonus}
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(Position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ", доход с учётом премии: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.profit)

p = Position()
print("\n<< Общая информация по сотруднику >>")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))

# Задание 4 *************************************************************************
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return 'Полицейская машина'
        else:
            return 'Гражданская машина'

    def full_info(self):
        return " {} {} Максимальная скорость {} км/ч ".format(self.color, self.name, str(self.speed))

    def go(self):
        return "Машина поехала"

    def stop(self):
        return"Машина остановилась"

    def turn(self):
        return"Машина повернула"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(160, "Black", "Vesta", False)
print(t_c.police() + t_c.full_info() + t_c.turn())

s_c = SportCar(250, "Red", "Audi", False)
print(s_c.police() + s_c.full_info() + s_c.go())

w_c = WorkCar(50, "Brown", "UAZ", False)
print(w_c.police() + w_c.full_info() + w_c.stop())

p_c = PoliceCar(400, "White", "Bugatti", True)
print(p_c.police() + p_c.full_info() + p_c.go())


# Задание 5 ***************************************************************
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Запускается'

    def stop(self):
        return f'{self.name} остановлен'

    def turn_right(self):
        return f'{self.name} Повернул на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} авто {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше, чем разрешено в городе'
        else:
            return f'Скорость {self.name} нормальная для города'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость работы автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше, чем разрешено'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} для отдела полиции'
        else:
            return f'{self.name} не для отдела полиции'


Ferrari = SportCar(100, 'красный', 'Ferrari', False)
Kia = TownCar(30, 'черный', 'Kia', False)
BMW = WorkCar(70, 'зеленный', 'BMW', True)
hyundai = PoliceCar(110, 'Blue',  'hyundai', True)
print(BMW.turn_left())
print(f'Когда {Kia.turn_right()}, тогда {Ferrari.stop()}')
print(f'{BMW.name} цвет- {BMW.color}')
print(f'Is {Ferrari.name} полицейская машина? {Ferrari.is_police}')
print(f'Is {BMW.name}  полицейская машина? {BMW.is_police}')
print(Ferrari.show_speed())
print(Kia.show_speed())
print(hyundai.police())
print(BMW.show_speed())


# Задание 6 ****************************************************************
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())