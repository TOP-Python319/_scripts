class Error(Exception):
    """Базовый класс для других исключений проекта"""


class InputError(Error):
    """Класс исключений, связанных с вводом данных

    Attributes:
        expression -- введенное выражение
        message -- текст сообщения об ошибке
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


x = input('Введите положительное целое число: ')
try:
    x = int(x)
    if x < 0:
        raise InputError(f'{x} не положительное число', '-> Допустимы только положительные числа!!!')
except ValueError:
    print('Вы ввели не число!!!')
except InputError as e:
    print(e.args[0])
    print(e.args[1])