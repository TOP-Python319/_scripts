# декоратор - это функция, которая может обернуть другую функцию для того чтобы
# изменить или расширить её функциональность.

# в python функции это функции высшего порядка
# функция высшего порядка это функция, которая может принимать в качестве аргументов другие функции и возвращать другие функции


# я хочу расширить функциональность функции say_hello() не изменяя её

# если вы описываете декоратор, то все аргументы, которые вы в него принимаете, лучше добавлять через *args, **kwargs

def decorator(func: callable) -> callable:

    # *args произвольное количество позиционных аргументов
    # **kwargs произвольное количество именнованных аргументов
    def inner(*args, **kwargs):
        print('Start decorator')
        func(*args, **kwargs)
        print('Finish decorator')

    return inner


def say_hello(name, surname):
    print(f'Hello {name} {surname}!')


def say_bye(name, surname, *, age):
    print(f'Bye {name} {surname} {age}!')


say_hello = decorator(func=say_hello)
print(say_hello)
say_hello('Ivan', 'Ivanov')

print('-------')

say_bye = decorator(func=say_bye)
print(say_bye)
say_bye('Petr', 'Petrov', age=18)