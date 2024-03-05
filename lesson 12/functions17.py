# функция получает на вход целое число от 0 до бесконечности
# выводит на печать сумму его цифр

# число вводит использователь

# Ввод:
# 12345

# Выход:
# 15


digit = int(input('Введите целое число: '))


def print_digits_sum_slow(n):
    str_n = str(n)
    total = 0
    for sign in str_n: # "12345", "1", "2", "3"...
        total += int(sign)

    print(total)


print_digits_sum_slow(digit)


def print_digits_sum_fast(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print(total)


print_digits_sum_fast(digit)