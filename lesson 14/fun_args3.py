def print_args_num(num, *args):
    print(*args * num)
    print()

# num = 3
# args = (1, 2, 3)
    
# если print(*args * num)
# кортеж 1,2,3 повторяется num раз
# после чего он распакоывается в print() с помощью *
# print(1,2,3,1,2,3,1,2,3)
    
# если print(args * num)
# кортеж 1,2,3 повторяется num раз
# но он не распаковывается в print()
# print((1,2,3,1,2,3,1,2,3))


print_args_num(6, 1, 2, 3)

print_args_num(2, 'a', 'b', 'c', 1, 10, 123, 'd', 100)