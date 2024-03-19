# reduce - сигнатура функция reduce(func, iterable[, initializer])
# функция которая применяет функцию func к элементам из iterable
# и возвращает единственный элемент

# initializer - начальное значение, если не указывать, то
# первый элемент в iterable


from functools import reduce

d = [1, 2, 3, 4, 5]


def multiply(x, y):
    return x * y


print(reduce(multiply, d))


def summator(x, y):
    return x + y


print(reduce(summator, d))

print(reduce(lambda x, y: x + y, d))