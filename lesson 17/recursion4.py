def fib_r(n):
    if n == 0:
        return 0  # базовый случай
    if n == 1:
        return 1  # базовый случай
    return fib_r(n - 1) + fib_r(n - 2)

print(fib_r(20))
    