# метод get(<ключ>, <значение по умолчанию>)
# возвращает значение по ключу,
# но если такого ключа нет, то
# возвращает значение по умолчанию
# при этом, новый ключ не создаётся

info = {
    'name': 'Ivan',
    'age': 30,
    'job': 'coder',
}

info['name']
# 'Ivan'
info['name'] = 'Alexander'
info
# {'name': 'Alexander', 'age': 30, 'job': 'coder'}
info['email'] = 'test@yahoo.com'
info
# {'name': 'Alexander', 'age': 30, 'job': 'coder', 'email': 'test@yahoo.com'}
# info['salary']  # нет такого ключа
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'salary'


##########

numbers = [1, 1, 1, 1, 10, 10, 3, 10, 10, 'hi', 7, 9, 10, 10, 'hi', 7]
# список чисел, некоторые повторяется
# посчитать сколько какое число повторяется

# записать в словарь пары число: количество повторений

result = {}
for n in numbers:  # последовательно перебираем 1 1 1 1 10 10 3
    result[n] = result.get(n, 0) + 1 

print(result)
