def factorial(n: int) -> int:
    """Факториал"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


x: int = 5
print(factorial(x))
