text = 'python is not a snake'

x = 'строчка'
# len(x)
7
x[7]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
x[6]
# 'а'
len('')
# 0
len(' ')
# 1
len('/n')
# 2
len('\n')
# 1
x = 'one\ntwo'
print(x)
# one
# two
len(x)
# 7
s_digits = (1, 3, 5, 7, 11, 13, 17, 19, 23)
s_digits[0]
# 1
s_digits[7]
# 19
len(s_digits)
# 9