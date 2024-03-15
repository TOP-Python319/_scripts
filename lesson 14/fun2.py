# именнованные аргументы можно вызывать в любом порядке
print('Hello', 'World!', 'I', 'am', 'learning', 'Python!', sep=' ', end='\n\n')
print('Hello', 'World!', 'I', 'am', 'learning', 'Python!', end='\n\n', sep=' ')


print('Hello', 'World!', 'I', 'am', 'learning', 'Python!')


print(int('1001', 2))  # аргумент 2 означает, что число 1001 записано в двоичной системе
print(int('1001', 8))  # аргумент 2 означает, что число 1001 записано в восьмеричной системе
print(int('1001', 10))  # аргумент 2 означает, что число 1001 записано в десятичной системе
print(int('1001', 16))  # аргумент 2 означает, что число 1001 записано в шестнадцатиричной системе
# в функции int, 2-ой аргумент означает основание системы счисления
# в функции int 2-ой параметр имеет значение по умлочанию 10

print()


# функция с параметром по умолчанию
# по умолчанию параметр exponent равен 2
def raise_to_power(base, exponent=2):
    """Calculate the base raised to the exponent.

    Args:
        base (int or float): The base number.
        exponent (int or float, optional): The exponent to raise the base to. Defaults to 2.

    Returns:
        int or float: The result of base raised to the exponent.
    """
    return base ** exponent


print(raise_to_power(11))
print(raise_to_power(11, 2))
print(raise_to_power(11, 3))
print(raise_to_power(11, 4))
print(raise_to_power(11, 5))
print(raise_to_power(11, 6))