cities = ['Moscow', 'Perm', 'Saratov', 'Vladivostok', 'Sochi']

# так делать можно, но не надо
# i = 0
# for city in cities:
#     print(f'{i}. {city}')
#     i += 1

# cities = ['Moscow', 'Perm', 'Saratov', 'Vladivostok', 'Sochi']
# после enumerate()
# cities = [(0, 'Moscow'), (1, 'Perm'), (2, 'Saratov'), (3, 'Vladivostok'), (4, 'Sochi')]

# for index, city in enumerate(cities):
#     print(f'{index}. {city}')

# >>>: 0. Moscow
# >>>: 1. Perm
# >>>: 2. Saratov
# >>>: 3. Vladivostok
# >>>: 4. Sochi


for index, city in enumerate(cities, 1):
    print(f'{index}. {city}')

# >>>: 1. Moscow
# >>>: 2. Perm
# >>>: 3. Saratov
# >>>: 4. Vladivostok
# >>>: 5. Sochi