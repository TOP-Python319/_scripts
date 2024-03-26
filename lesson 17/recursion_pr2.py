# функция принимает n и распечатывает на экране
# возрастающая последовательность от 1 до n

# Вход:
# 7
# Выход:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

def print_increase(n: int) -> None:
    if n >= 1:        
        print_increase(n - 1)
        print(n)


print_increase(7)

# print(factorial_r(4))
# factorial_r(4)  # (4 * (3 * (2 * (1)))) = 24
# factrorial_r(4) = 4 * factorial_r(3)
#                       | 3 * factorial_r(2)
#                             | 2 * factorial_r(1)
#                                   | 1
