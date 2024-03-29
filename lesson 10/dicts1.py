cities = {
    'Индия': 'Нью-Дели', 
    'Китай': 'Пекин', 
    'Чехия': 'Прага'
}

print(cities)
# >>>: {'Индия': 'Нью-Дели', 'Китай': 'Пекин', 'Чехия': 'Прага'}
type(cities)
# >>>: <class 'dict'>
cities['Индия']
# >>>: 'Нью-Дели'
cities['Китай']
# >>>: 'Пекин'
cities['Чехия']
# >>>: 'Прага'

# ключом не могут быть изменяемые объекты: list(), set(), dict()
# то же справедливо и для set()

abstract_dict = {
    10: 'тип int может быть ключом',
    'text': 'тип str может быть ключом',
    12.1: 'тип float может быть ключом',
    (1, 2, 3): 'тип tuple может быть ключом',
    frozenset((1, 2, 3)): 'тип данных frozenset может быть ключом',
    True: 'тип данных bool может быть ключом',
    None: 'тип данных NoneType может быть ключом'
}

# broken_dict = {
#     [1, 2, 3]: 'тип list не может быть ключом',
#     set((1, 2, 3)): 'тип данных set не может быть ключом',
#     {'one': 1, 'two': 2, 'three': 3}: 'тип данных не может быть ключом'
# }

print()
print(len(cities))
for key in cities:
    print(f'ключ = {key} значение = {cities[key]}') 
# 1 итерация: key = 'Индия', cities[key] == cities['Индия'] == 'Нью-Дели'
# 2 итерация: key = 'Китай', cities[key] == cities['Китай'] == 'Пекин'

# ключи в словаре уникальные
cities2 = {
    'Индия': 'Нью-Дели', 
    'Китай': 'Пекин', 
    'Чехия': 'Прага',
    'Индия': 'Мумбаи'
}
