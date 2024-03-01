# метод setdefault(<ключ>, <значение по умолчанию>)
# возвращает значение по ключу,
# но если такого ключа нет, то
# создаётся новый ключ и
# ему присваивается значение по умолчанию 

info = {
    'name': 'Alexey',
    'age': 46
}

info
# {'name': 'Alexey', 'age': 46}
info.get('name')
# 'Alexey'
info.setdefault('name')
# 'Alexey'
info.get('salary')
info
# {'name': 'Alexey', 'age': 46}
info.setdefault('salary')
info
# {'name': 'Alexey', 'age': 46, 'salary': None}
info.setdefault('salary', 10000)
info
# {'name': 'Alexey', 'age': 46, 'salary': None}
info.setdefault('mortgage', 123456)
# 123456
info
# {'name': 'Alexey', 'age': 46, 'salary': None, 'mortgage': 123456}
