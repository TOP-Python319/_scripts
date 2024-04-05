def header(func):

    def inner(*args, **kwargs):
        print('<header>')
        func(*args, **kwargs)
        print('</header>')

    return inner


def h1(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def say(name, surname, age):
    print(f'{name} {surname} {age}')


say = header(h1(say))
say('Ivan', 'Ivanov', 27)