# def factorial(n):  # 1 * 2 * 3 * ... * n
#     mult = 1
#     while n >= 1:
#         mult *= n
#         n -= 1
#     return mult

# print(factorial(1000))


def factorial_r(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:  # базовый случай, выход из функции
        return 1
    else:       # рекурсивный случай, функция вызывает сама себя
        return n * factorial_r(n - 1)

# глубина рекурсии в python около 1000
print(factorial_r(5))
# n = 5
# 5 * (n - 1)
# 4 * (n - 1)
# 3 * (n - 1)
# 2 * (n - 1)
# 1 * (n - 1)


print(factorial_r(4))
# factorial_r(4)  # (4 * (3 * (2 * (1)))) = 24
# factrorial_r(4) = 4 * factorial_r(3)
#                       | 3 * factorial_r(2)
#                             | 2 * factorial_r(1)
#                                   | 1


# глубина рекурсии в python около 1000, но её можно увеличить
# import sys
# sys.setrecursionlimit(3000)
# print(factorial_r(1500))