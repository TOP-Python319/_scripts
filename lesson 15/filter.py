# filter() - сигнатура filter(func, iterable)
# функция которая применяет функцию func к каждому элементу из iterable
# и возвращает итератор с элементами, для которых функция func вернула True

d = [-1, -3, -4, 0, 10, 11, 12, -2, -9]

def get_positive(x):
    return x > 0

print(list(filter(get_positive, d)))
print(*filter(get_positive, d))

print(*filter(lambda x: x > 0, d))