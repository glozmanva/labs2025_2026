from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.color = color

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.FIGURE_TYPE,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )