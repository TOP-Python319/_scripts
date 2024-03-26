# функция принимает n и распечатывает на экране
# убывающую последовательность от n до 1

# Вход:
# 7
# Выход:
# 7
# 6
# 5
# 4
# 3
# 2
# 1

def print_decrease(n: int) -> None:
    if n >= 1:
        print(n)
        print_decrease(n - 1)


print_decrease(7)