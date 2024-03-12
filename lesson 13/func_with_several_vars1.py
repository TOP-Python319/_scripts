# функция возвращающая число в степенях 2, 3, 4

def calc_powers(number):  # возвращает кортеж из трёх значений, которые можно распаковать в три переменные или в один кортеж
    return number**2, number**3, number**4

def print_powers(number):  # не возвращает ничего, просто печатает значение в терминал
    print(number**2, number**3, number**4)


n = int(input('Введите число: '))

n_in_2, n_in_3, n_in_4 = calc_powers(n)
n_tuple = calc_powers(n)
# функция вернула три значения в кортеже
# python позволяет распаковывать коллекции сразу в переменные
