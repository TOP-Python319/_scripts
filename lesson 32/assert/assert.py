def divine(x, y):
    assert y != 0, "Делить на ноль нельзя!"
    return x / y


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(divine(num1, num2))
