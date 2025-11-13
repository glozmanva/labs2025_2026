from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Style


def main():

    rectangle = Rectangle(5, 5, "синего")
    circle = Circle(5, "зеленого")
    square = Square(5, "красного")


    print(rectangle)
    print(circle)
    print(square)

    print(Fore.BLUE + "Этот текст синего цвета!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()