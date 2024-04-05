# декоратор - это функция, которая может обернуть другую функцию для того чтобы
# изменить или расширить её функциональность.

# в python функции это функции высшего порядка
# функция высшего порядка это функция, которая может принимать в качестве аргументов другие функции и возвращать другие функции


def decorator(func: callable) -> callable:

    def inner():
        print('Start decorator')
        func()
        print('Finish decorator')

    return inner


def say_hello():
    print('Hello Python!')


d = decorator(func=say_hello)
print(d)
d()