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