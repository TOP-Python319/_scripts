year = int(input('Введите год: '))

if year % 100 == 0:
    print('YES')
else:
    print('NO')

if str(year)[-2:] == '00':
    print('YES')
else:
    print('NO')