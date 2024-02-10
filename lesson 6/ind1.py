text = 'Hello world!'

text
# 'Hello world!'
text
# 'Hello world!'
text + '!'
# 'Hello world!!'
text + '!!'
# 'Hello world!!!'


text = 'python is not a snake'

text
# 'python is not a snake'
type(text)
# <class 'str'>
text[0]
# 'p'
type(text[0])
# <class 'str'>
char = 'x'
char[0]
# 'x'
empty_string = ''
empty_string[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range