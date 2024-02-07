# оператор is

v1 = 'Python'
v2 = 'Django'
id(v1)
# 140652206895088
id(v2)
# 140652203315184
v3 = 'Python'
id(v3)
# 140652206895088
v1 == v2
# False
v1 == v3
# True
v1 is v3
# True
# v1 = ['python', 3]
# v3 = ['python', 3]
id(v1)
# 140652205651776
id(v3)
# 140652205587776
v1 == v3
# True
v1 is v3
# False


# оператор is not

v1 is not v3
# True
not v1 is v3
# True


