# изменяемые типы данных: множества (set), словари (dict), списки (list)

def append(element, seq=[]):
    seq.append(element)
    return seq


print(append(10, [1, 2, 3]))  # [1, 2, 3, 10]
print(append(5, [1]))  # [1, 5]
print(append(5, []))  # [5]
print(append(3, [4, 5]))  # [4, 5, 3]

print()

print(append(10))  # [10]
print(append(1))  # [1], нет, правильно [10, 1]
print(append(500))  # [500], нет, правильно [10, 1, 500]
print(append(1000))  # [1000], нет, правильно [10, 1, 500, 1000]


# так как список это изменяемый тип данных, то при каждом вызове функции append()
# мы меняем список, а не создаем новый список
