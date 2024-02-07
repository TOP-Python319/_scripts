d1 = int(input('Введите число: '))

if d1 % 2 == 0:
    print('Числое чётное')
else:
    print('Число нечётное')


# в js ИЛИ это ||
# в python ИЛИ это or
# в js И это &&
# в python И это and
# в js НЕ это !
# в python НЕ это not

1 == 1 or 2 == 5 and 3 == 0  # 1
# True
True or False and False  # 2
# True
True or False  # 3
# True


1 < 10 < 100
# True
1 < 10 and 10 < 100
# True

# высший приоритет ()
# not
# and
# or
