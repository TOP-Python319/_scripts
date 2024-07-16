def sum_extended(*args):
    print(type(args))
    return sum(args)


# sum(1, 2, 3, 4, 5)
print(sum_extended(1, 2, 3, 4, 5, 100, 1000, 2.7, 3.1415926, -42))


#################################################################
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3, 4, 5, 100, 1000, 2.7, 3.1415926, -42)


#################################################################
def abstr(char, *args):
    for arg in args:
        print(f'{char} {arg}')


abstr('a', 1, 2, 3, 4, 5, 100, 1000, 'py')
