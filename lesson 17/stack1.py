def greeting(name):
    print(f'Привет {name}')
    greeting2(name)
    print(f'Приято познакомиться!')
    goodbye()
    print('Конец выполнения')


def greeting2(name):
    print(f'Как дела {name}')


def goodbye():
    print('Пока!')


greeting('Пётр')