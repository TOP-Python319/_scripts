cities = ['Moscow', 'Perm', 'Saratov', 'Vladivostok', 'Sochi']

# так делать можно, но не надо
# i = 0
# for city in cities:
#     print(f'{i}. {city}')
#     i += 1


# переменную цикла можно называть как угодно
# для абстрактных объектов лучше называть i, j, k
# for i in range(1, 11):
#      print(i)

# >>>: 1
# >>>: 2
# >>>: 3
# >>>: 4
# >>>: 5
# >>>: 6
# >>>: 7
# >>>: 8
# >>>: 9
# >>>: 10


people = [
    ['Mars', 'Kramer'],
    ['Oleg', 'Ivanov'],
    ['Anna', 'Great'],
    ['Stanislav', 'Petrov']
]

# for person in people:
#     print(person)
# >>>: ['Mars', 'Kramer']
# >>>: ['Oleg', 'Ivanov']
# >>>: ['Anna', 'Great']
# >>>: ['Stanislav', 'Petrov']

# for person in people:
#     print(f'name: {person[0]}, last_name: {person[1]}')
# >>>: name: Mars, last_name: Kramer
# >>>: name: Oleg, last_name: Ivanov
# >>>: name: Anna, last_name: Great
# >>>: name: Stanislav, last_name: Petrov

for name, last_name in people:
    print(f'name: {name}, last_name: {last_name}')

