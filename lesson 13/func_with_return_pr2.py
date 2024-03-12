# пользователь вводит значения катетов треугольника
# программа считает гипотенузу и возвращает значение

# a² + b² = c²

import math  # импортируется модуль работы с математикой


def calculate_hypotenuse(a: float, b: float) -> float:
    return math.sqrt(pow(a, 2) + pow(b, 2))  # .sqrt() - извлечение квадратного корня

a = float(input('Введите длину первого катета: '))
b = float(input('Введите длину второго катета: '))

print(calculate_hypotenuse(a, b))

