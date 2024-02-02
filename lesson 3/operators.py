>>> 2 + 2
4
>>> 1 + 3
4
>>> 10 + 2
12
>>> print(10 + 2)
12
>>> True + False
1
>>> 'a' + 'bc'
'abc'
>>> 
>>> 
>>> 
>>> x = 5
>>> x = 5 + 10
>>> print(x)
15
>>> 
>>> print(x = 5 + 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'x' is an invalid keyword argument for print()
>>> 


===================================================
10 + 11 -> выражение
x = 10 + 11 -> инструкция

print(10 + 11) -> 10 + 11 выражение и print(10 + 11) это выражение с выражением внутри


print(x = 10 + 11) -> x = 10 + 11 инструкция и она ничего не возвращает, значит её нельзя передать никуда
====================================================

Операторы:

>>> 1 + 2

3
>>> 4 - 3
1

>>> 3 * 4
12

>>> 9 / 3
3.0

>>> 9 // 4  # целочисленное деление
2
>>> 9 % 4  # остаток от деления
1
>>> 9 ** 2  # возведение в степень
81
>>> 'a' + 'b'
'ab'
>>> 

Переменные с разными типами данных не взаимодействуют друг с другом без явного преобразования типов
>>> 'a' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'a' + True
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "bool") to str
>>> 'b' + 'a' + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> 1 + True
2

>>> 'a' * 10  # в данном случае мы говорим интерпретатору повторить строку 'a' десять раз
'aaaaaaaaaa'

