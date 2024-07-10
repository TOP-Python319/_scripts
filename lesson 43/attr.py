def multiply(x, y):
    return x * y


print(multiply(2, 10))


############################################################
def multiply_10(x, y=10):
    return x * y


print(multiply_10(9))
print(multiply_10(9, 5))


############################################################
def add(x, y, z):
    return x + y + z


print(add(5, 7, 4))
print(add(y=7, z=4, x=5))
print(add(5, y=7, z=4))
# print(add(7, y=4, 5))  сначала позиционные аргументы, потом именные


############################################################
def repeat_sequence(text, *, times, order):  # в данном случае, * означает, что аргументы, которые мы передали после этого символа, могу передаваться только в качестве именных аргументов
    if order == 'ASC':
        return sorted(list(text * times))
    else:
        return sorted(list(text * times))[::-1]


print(repeat_sequence('abc', times=5, order='ASC'))
print(repeat_sequence('cda', times=10, order='DESC'))
# print(repeat_sequence('cda', 10, order='DESC'))  # не сработает, потому что times и order должны передаваться только как именнованые аргументы


############################################################
def repeat_sequence(*, text, times, order):  # теперь все аргументы должны передаваться только как именнованые
    if order == 'ASC':
        return sorted(list(text * times))
    else:
        return sorted(list(text * times))[::-1]


print(repeat_sequence(text='abc', times=5, order='ASC'))
print(repeat_sequence(text='cda', times=10, order='DESC'))
