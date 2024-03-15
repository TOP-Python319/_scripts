# функция matrix()
# функция matrix() создает матрицу заданного размера

# matrix() - возвращается матрица 1x1, в котором число равно нулю
# matrix(n) - возвращается матрица nxn, в которой все числа нули
# matrix(n, m) - возвращается матрица n строк и m столбцов, в которой все числа нули
# matrix(n, m, value) - возвращается матрица n строк и m столбцов, в которой все числа value

# matrix()
# [[0]]

# matrix(3)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrix(3, 4)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# matrix(3, 4, 1)
# [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]

print(matrix(3, 4, 1))
print(matrix(3, 4))
print(matrix(3))
print(matrix())
print(matrix(value=10))
print(matrix(m=10, value=0))
print(matrix(n=10, value=0))
print(matrix(n=10, m=0, value=0))
