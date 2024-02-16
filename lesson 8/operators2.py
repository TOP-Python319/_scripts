age = int(input('Введите возраст: '))
sex = input('Введите пол: ')

if 10 <= age <= 15 and sex == 'f':
    print('YES')
else:
    print('NO')

# <значение если условие True> if <условие> else <значение если условие False>
print('YES' if 10 <= age <= 15 and sex == 'f' else 'N')