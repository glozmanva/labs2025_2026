from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.color = color

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.2f}.'.format(
            self.FIGURE_TYPE,
            self.color.color,
            self.radius,
            self.area()
        )