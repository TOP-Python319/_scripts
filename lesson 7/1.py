tuple_1 = (1, 2, 3, 4, 5)
tuple_1
# >>>: (1, 2, 3, 4, 5)


# tuple (он же кортеж) является неизменяемым типом данных
# мы не можем добавлять в него или удалять элементы
# tuple_1 + 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "int") to tuple
# 
# tuple_1.append(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'


# list (список) отличается от tuple (кортеж), тем что список изменяемый
# list поддерживает методы append(), extend(), pop()
list_1 = [1, 2, 3, 4, 5]
list_1.append(6)
list_1
# >>>: [1, 2, 3, 4, 5, 6]
id(list_1)
# >>>: 140522670661632
list_1.append(7)
id(list_1)
# >>>: 140522670661632
# список — изменяемый тип данных, это значит, что
# когда мы изменяем его (добавляем или удаляем элемент)
# id списка не меняется, он остаётся на том же адресе памяти


# в свою очередь int является неизменямым типом данных
# когда мы что-то делаем с числом, на самом деле мы
# пересоздаём переменную, id меняется
x = 1
id(x)
# >>>: 140522682203944
x = x + 1
id(x)
# >>>: 140522682203976


# та же самая ситуация и со строкой (str)
# каждый раз когда мы что-то добавляем в строку
# мы пересоздаём переменную
text = 'Python'
id(text)
# >>>: 140522681637376
text = text + '!!!'
text
# >>>: 'Python!!!'
id(text)
# >>>: 140522676491760
