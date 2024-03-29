# через литерал словаря
d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

# через функцию dict с параметрами
d2 = dict(a=1, b=2, c=3)  # каждый параметр становится ключом с типом str
# print('Hello world!', sep='\t', end='\n')
# d2 = dict(1=one, 2=two, 3=three)  # параметр может быть только текстовым
# d2 = {1: 'one', 2: 'two', 3:'three'}

d3 = dict([('a', 1), ('b', 2), ('c', 3)])
# d3 = dict(((1, 'one'), (2, 'two'), (3, 'three')))

# dict.fromkeys() создаёт cловарь из итерируемого объекта
d4 = dict.fromkeys(range(0, 11)) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
d5 = dict.fromkeys(range(0, 11), 'измените значение')