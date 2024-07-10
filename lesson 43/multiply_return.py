###################################################
def divide(x, y):
    return x // y, x % y


quotient, remainder = divide(10, 3)
print(quotient)
print(remainder)

###################################################
quotient, remainder = divide(17, 9)
print(quotient)
print(remainder)


def divide2(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder


print(divide(10, 3))
print(divide2(10, 3))


x, y = divide(10, 3)
print(x)
print(y)

q, r = divide2(10, 3)
print(q)
print(r)