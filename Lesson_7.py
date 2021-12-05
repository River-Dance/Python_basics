# Задание 1 *************************************************************************
class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % j
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 3, 1]]
m = Matrix(a)
mm = Matrix(b)

print("\nМатрица №1")
print(m.__str__(), "\n")

print("Матрица №2")
print(mm.__str__(), "\n")

print("Сумма матриц №1 и №2")
print(m + mm)

# Задание 2 *************************************************************************
from abc import ABC

from typing import Any


class AbstractClothes(ABC):
    result = 0


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        """ Расход ткани """
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        """ Узнать размер """
        return self._measuring

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.measuring

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.measuring

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('', 5)
    print(coat)

    suit = Suit('', 178)
    print(suit)

    print('Общий расход', coat.total_tissue_required, 'кв. метров ткани')

# Задание 3 *************************************************************************
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(16)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))