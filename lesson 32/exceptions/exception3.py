class Error(Exception):
    """Базовый класс для других исключений проекта"""


class ValueTooSmallError(Error):
    """Исключение, если значение мало"""


class ValueTooLargeError(Error):
    """Исключение, если значение велико"""


number = 10


while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()


print("Congratulations! You guessed it correctly.")
