# функция-замыкание create_dict(), 
# которая сохраняет в себе все переданные ей аргументы и выводит в виде словаря


def create_dict() -> callable:
    d = {}
    counter = 1
    def inner(value) -> dict:
        nonlocal counter
        d[counter] = value
        counter += 1
        return d

    return inner


d1 = create_dict()
print(d1('python'))  # {1: 'python'}
print(d1('rust'))  # {1: 'python', 2: 'rust'}

d2 = create_dict()
print(d2('java')) # {1: 'java'}
