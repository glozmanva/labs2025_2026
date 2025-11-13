import sys
import math


def read_coefficient(param_index, prompt_message):

    coefficient = None
    if len(sys.argv) > param_index:
        try:
            coefficient = float(sys.argv[param_index])
            return coefficient
        except ValueError:
            print("Некорректное значение в аргументах. Требуется ввод с клавиатуры.")

    while True:
        print(prompt_message)
        try:
            coefficient = float(input())
            return coefficient
        except ValueError:
            print("Ошибка: введите действительное число.")


def solve_biquadratic(a, b, c):
    roots = []

    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        y1 = (-b + math.sqrt(discriminant)) / (2 * a)
        y2 = (-b - math.sqrt(discriminant)) / (2 * a)


        for y in [y1, y2]:
            if y > 0:
                x1 = math.sqrt(y)
                x2 = -math.sqrt(y)
                roots.extend([x1, x2])
            elif y == 0:
                roots.append(0.0)

    return sorted(roots)


def main():

    print("Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0")

    a = read_coefficient(1, "Введите коэффициент A:")
    b = read_coefficient(2, "Введите коэффициент B:")
    c = read_coefficient(3, "Введите коэффициент C:")

    if a == 0:
        print("Ошибка: коэффициент A не может быть нулем для биквадратного уравнения.")
        return

    roots = solve_biquadratic(a, b, c)

    if not roots:
        print("Действительных корней нет")
    else:
        print(f"Найдено корней: {len(roots)}")
        for i, root in enumerate(roots, 1):
            print(f"Корень {i}: {root:.4f}")


if __name__ == "__main__":
    main()