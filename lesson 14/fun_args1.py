print('a', 'b', 'c', 1, 10, 123, 'd', 100)



def print_args(*args):
    print(type(args))
    print(args)
    print()

print_args()
print_args(1, 2, 3)
print_args('a', 'b', 'c', 1, 10, 123, 'd', 100)

# принято называть такие переменные *args, можно задать своё название, но
# не стоит
# это на уровне соглашения

# такой параметр может быть только один в функции
