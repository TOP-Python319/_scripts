# map(func, *iterables) - сигнатура функции
# функция которая применяет функцию func к каждому элементу из iterables

def square(x):
    return x**2


l = [1, 2, 3, 4, 5]
print(*map(square, l), sep=',')
# объект map
# который мы распаковали
# print(1, 4, 9, 16, 25)
print(list(map(square, l)))
print(*list(map(square, l)))

print(list(map(lambda x: x**2, l)))