from functools import wraps


def h1(func):
    
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


# @h1  # say = h1(say)
def say(name, surname, age):
    """Функция, которая выводит имя фамилию и возраст"""
    print(f'{name} {surname} {age}')


# say('Ivan', 'Ivanov', 27)

print('До декорирования', say.__name__)
print('До декорирования', say.__doc__)
say = h1(say)
print('После декорирования', say.__name__)
print('После декорирования', say.__doc__)

# после декорирования функция теряет имя и docstring