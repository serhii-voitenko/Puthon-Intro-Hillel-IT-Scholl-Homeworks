"""
Геометрические фигуры
Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с методами подсчета
 площади и периметра. Методы должны возвращать значение, а не принтить
"""


class Figure:
    """ Общий класс фигур """
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (self.side1 + self.side2) * 2


class Triangle(Figure):
    """ Треугольник, наследуется от Фигуры """
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2)
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        import math
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


class Cube(Figure):
    """ Квадрат, наследуется от Фигуры"""
    def __init__(self, side1):
        super().__init__(self, side1)
        self.side1 = float(side1)
        self.side2 = float(side1)


class Rectangle(Figure):
    """ Прямоугольник, наследуется от Фигуры"""
    def __init__(self, side1, side2):
        super().__init__(side1, side2)
        self.side1 = float(side1)
        self.side2 = float(side2)


print(f'Площаь треугольника: {Triangle(3, 3, 4).area()}')
print(f'Периметр треугольника: {Triangle(3, 3, 4).perimeter()}')
print(f'Периметр квадрата: {Cube(3).perimeter()}')
print(f'Площадь квадрата: {Cube(3).area()}')
print(f'Площадь прямоугольника: {Rectangle(3, 4).area()}')
print(f'Периметр прямоугольника: {Rectangle(3, 4).perimeter()}')

