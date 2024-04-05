# декоратор text_decor, который оборачивает вызов декорированно функции фразами Hello, Goodbye

def text_decor(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye')
    return wrapper


@text_decor
def world():
    print('Это обёрнутая функция.')

world()
# Hello
# Это обёрнутая функция
# Goodbye

@text_decor
def pow(x, y):
    print(x ** y)

pow(2, 3)