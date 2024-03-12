# пользователь вводит значения катетов треугольника
# программа считает гипотенузу и возвращает значение

# a² + b² = c²


def calculate_hypotenuse(a: float, b: float) -> float:
    return (a ** 2 + b ** 2)  ** 0.5

a = float(input('Введите длину первого катета: '))
b = float(input('Введите длину второго катета: '))

print(calculate_hypotenuse(a, b))

