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


@header  # say = header(h1(say))
@h1  # say = h1(say)
def say(name, surname, age):
    print(f'{name} {surname} {age}')


@header  # bye = header(bye)
def bye(name, surname, age):
    print(f'{name} {surname} {age}')


say('Ivan', 'Ivanov', 27)
print('-----------------')
bye('Ivan', 'Ivanov', 27)


# поиск файла
# открытие файла на чтение
# выставление специальных режимов
# переменные, которые задали аналитики, пробрасывались в программу