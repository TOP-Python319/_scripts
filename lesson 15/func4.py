# min() - функции высшего порядка
# max() - функции высшего порядка
# sorted() - функции высшего порядка

digits = [10, -10, 20, -1000, -13, 57, 63]
print(min(digits))
print(max(digits))
print(sorted(digits))

print()
# Вывод:
# -1000
# 63
# [-1000, -13, 10, 20, 57, 63]

# у всех этих функций есть необязательный
# аргумент key, который принимает функцию

print(min(digits, key=abs))
print(max(digits, key=abs))
print(sorted(digits, key=abs))