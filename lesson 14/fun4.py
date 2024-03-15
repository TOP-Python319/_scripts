def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq


print(append(10))  # [10]
print(append(1))  # [1]
print(append(500))  # [500]
print(append(1000))  # [1000]


# При написании ф-ций, важные параметры стоит указывать первыми

# Именнованные аргументы часто используют со значениями по умолчанию

# Позиционные аргументы ВСЕГДА должны быть перед именнованными аргументами