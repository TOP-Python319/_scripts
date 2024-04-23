функция факториала
def factorial(x: int) -> int:
    """ 
    функция факториала
    int -> int
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """

    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)