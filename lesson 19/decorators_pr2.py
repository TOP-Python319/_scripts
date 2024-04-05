# напишем декоратор, который два раза вызывает декорированную функцию


def reapeter(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@reapeter
def pow(x, y):
    print(x ** y)


@reapeter
def mod_print(*args, **kwargs):
    print(*args, **kwargs)
    pow(2, 3)


# pow(2, 3)
# 8
# 8

mod_print('Hello world!', '!!!', 'python', '!')