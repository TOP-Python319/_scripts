# параметр *args должен распологаться в конце функции


def print_args_num(num, *args):
    print(*args * num)
    print()


print_args_num(6, 1, 2, 3)
print_args_num(6, 1, 2, 3, 4)
print_args_num(6, 1, 2, 3, 4, 5)
print_args_num(2, 'a', 'b', 'c', 1, 10, 123, 'd', 100)


def print_args_num2(*args, num):
    print(*args * num)
    print()

print_args_num2(6, 1, 2, num=3)
print_args_num2(6, 1, 2, 3, num=4)
print_args_num2(6, 1, 2, 3, 4, num=5)
print_args_num2(2, 'a', 'b', 'c', 1, 10, 123, 'd', num=100)
