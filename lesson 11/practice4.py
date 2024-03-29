# Напишите программу, которая будет превращать натуральное число 
# в строку, заменяя все цифры в числе на слова:

# 0 на zero;
# 1 на one;
# 2 на two;
# 3 на three;
# 4 на four;
# 5 на five;
# 6 на six;
# 7 на seven;
# 8 на eight;
# 9 на nine.

# **Формат входных данных:**
# На вход программе подается натуральное число.

# **Формат выходных данных**
# Программа должна вывести строковое представление числа.

# *Примечание. Используйте словарь вместо условного оператора.*

# **Пример ввода 1:**
# 230

# **Пример вывода 1:**
# two three zero

# **Пример ввода 2:**
# 7

# **Пример вывода 2:**
# seven

# **Пример ввода 3:**
# 11111111

# **Пример вывода 3:**
# one one one one one one one one

# **Пример ввода 4:**
# 83

# **Пример вывода 4:**
# eight three

d = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
} #  в словаре ключи имеют тип int

digits = input('Введите число: ') # str

for i in digits: # каждый i тоже str
    print(d[int(i)], end=' ')  # каждый i преобразуем в int
print()


# print(*[{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}[int(i)] for i in input()])