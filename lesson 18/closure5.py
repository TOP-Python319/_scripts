def add(a, b):
    return a + b

# print(add(10, 5))
# print(add(12, 7))


def counter(func: callable) -> callable:
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызвана {count} раз')
        return func(*args, **kwargs)

    return inner


c = counter(add)
c(10, 5)  # функция вызвана 1 раз
c(12, 7)  # функция вызвана 2 раз
c(30, 2)  # функция вызвана 3 раз

p = counter(print)
p('Hello')
p('Hello world')


