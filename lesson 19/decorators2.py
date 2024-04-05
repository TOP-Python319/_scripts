# декоратор - это функция, которая может обернуть другую функцию для того чтобы
# изменить или расширить её функциональность.

# в python функции это функции высшего порядка
# функция высшего порядка это функция, которая может принимать в качестве аргументов другие функции и возвращать другие функции


# я хочу расширить функциональность функции say_hello() не изменяя её


def decorator(func: callable) -> callable:

    def inner(x):
        print('Start decorator')
        func(x)
        print('Finish decorator')

    return inner


def say_hello(name):
    print(f'Hello {name}!')


def say_bye(name):
    print(f'Bye {name}!')


say_hello = decorator(func=say_hello)
print(say_hello)
say_hello(x='Python!')

print('-------')

say_bye = decorator(func=say_bye)
print(say_bye)
say_bye(x='world')