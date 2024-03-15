print(sum([3, 4, 5, 6, 7]))
print(sum((3, 4, 5, 6, 7)))
print(sum({3, 4, 5, 6, 7}))
# print(sum(3, 4, 5, 6, 7)) # не сработает, потому что sum принимает только один аргумент


def modified_sum(*args):
    return sum(args)


print(modified_sum(3, 4, 5, 6, 7))