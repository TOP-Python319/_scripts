cities = {
    'Индия': 'Нью-Дели', 
    'Китай': 'Пекин', 
    'Чехия': 'Прага',
    'Ирландия': 'Дублин',
    'Россия': 'Москва',
    'Турция': 'Анкара'
}

cities.keys()  # извлечение ключей
# dict_keys(['Индия', 'Китай', 'Чехия', 'Ирландия', 'Россия', 'Турция'])
type(cities.keys())
# <class 'dict_keys'>

cities.values()  # извлечение значений
# dict_values(['Нью-Дели', 'Пекин', 'Прага', 'Дублин', 'Москва', 'Анкара'])
type(cities.values())
# <class 'dict_values'>

cities.items()  # извлчение элементов (ключ, значение)
# dict_items([('Индия', 'Нью-Дели'), ('Китай', 'Пекин'), ('Чехия', 'Прага'), ('Ирландия', 'Дублин'), ('Россия', 'Москва'), ('Турция', 'Анкара')])
type(cities.values())
# <class 'dict_items'>

print()
for key in cities.keys():
    print(key)

print()
for value in cities.values():
    print(value)

print()
for item in cities.items():
    print(item)

print()
for item in cities.items():
    print(item[0], item[1])

print()
for country, city in cities.items():
    print(f'{country=}, {city=}')