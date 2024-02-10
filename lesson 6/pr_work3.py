n = int(input('Введите число: '))

if n % 2 == 1:
    print('нечётное')
else:
    if 2 <= n <= 5:
        print('чётное от 2 до 5')
    elif n > 20:
        print('чётное больше 20')
    else:
        print('чётное от 6 до 20')