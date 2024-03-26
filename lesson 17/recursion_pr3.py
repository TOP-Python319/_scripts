# на вход подаётся список целых чисел
# на выходе получаем сумму чисел

# Вход
# [1, 2, 3, 4]
# Выход
# 10

def list_sum_recursive(s: list) -> int:
    # базовый случай
    if len(s) == 1:
        return s[0]
    # рекурсивный случай
    else:
        return s[0] + list_sum_recursive(s[1:])


print(list_sum_recursive([1, 2, 3, 4]))
# 1 + [2, 3, 4]
#     2 + [3, 4]
#          3 + [4]
#              [4]