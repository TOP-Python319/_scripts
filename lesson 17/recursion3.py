# функция выдаст ошибку о том что достигнута максимальная глубина
# рекурсии
# def final_countdown(n):
#     print(n)
#     final_countdown(n - 1)
# final_countdown(10)


# у каждой рекурсивной функции, должен быть базовый случай
# и рекурсивный случай

def final_countdown(n):
    print(n)
    if n <= 0:  # базовый случай, случай когда функция себя не вызывает
        return
    else:  # рекурсивный случай, случай когда функция себя вызывает
        final_countdown(n - 1)

final_countdown(10)