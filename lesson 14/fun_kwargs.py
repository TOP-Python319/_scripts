def f(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print()


f()
f(a=1, b=2, c=3)
f(country='Russia', city='Moscow')

# параметр **kwargs является словарем и пишется в самом конце определения функции
# даже после *args

def x(a, b, *args, name='Maks', age=34, **kwargs):
    print(a, b)
    print(name, age)
    print(args)
    print(kwargs)
    print()


x(1, 2, 3, 4, 5, name='Max', age=34, job='Coder', country='Russia')
# 1 2
# Max 34
# (3, 4, 5)
# {'name': 'Max', 'age': 34, 'job': 'Coder', 'country': 'Russia'}

x(1, 2, name='Ivan', country='Russia', salary='2000')