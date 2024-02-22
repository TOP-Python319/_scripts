# (<выражение> for <переменная цикла> in <итерируемый объект> if <условие>)

# для каждого n из range(0, 11) сделай 2 в степени n
generator_object = (2 ** n for n in range(0, 11))

# не эквивалентно, но похоже по синтаксису
# for n in range(0, 11): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     2 ** n


>>> generator_object = (2 ** n for n in range(0, 11))
>>> type(generator_object
... )
<class 'generator'>
>>> generator_object
<generator object <genexpr> at 0x7f7a7a4c75e0>
>>> print(generator_object)
<generator object <genexpr> at 0x7f7a7a4c75e0>
>>> 
>>> for element in generator_object:
...     print(element)
... 
1
2
4
8
16
32
64
128
256
512
1024
>>> 
>>> for element in generator_object:
...     print(element)
... 
>>> generator_object = (2 ** n for n in range(0, 11))
>>> for element in generator_object:
...     print(element)
... 
1
2
4
8
16
32
64
128
256
512
1024
>>> for element in generator_object:
...     print(element)
... 
>>> generator_object = (2 ** n for n in range(0, 11))
>>> list(generator_object)
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
>>> list(generator_object)
[]
>>> generator_object = (2 ** n for n in range(0, 11))
>>> generator_object.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'generator' object has no attribute 'next'
>>> generator_object.__next__()
1
>>> generator_object.__next__()
2
>>> generator_object.__next__()
4
>>> generator_object.__next__()
8
>>> generator_object.__next__()
16
>>> generator_object.__next__()
32
>>> generator_object.__next__()
64
>>> generator_object.__next__()
128
>>> generator_object.__next__()
256
>>> generator_object.__next__()
512
>>> generator_object.__next__()
1024
>>> generator_object.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> generator_object.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> generator_object = (2 ** n for n in range(0, 11))
>>> generated_list = list(2 ** n for n in range(0, 11))
>>> generated_list
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
>>> type(generated_list)
<class 'list'>
