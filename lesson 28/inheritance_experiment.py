class NewStr(str):

    def append(self, item):
        return NewStr(self + str(item))


x = NewStr("hello")
x = x.append(1)
x = x.append(2)
x = x.append(3)
print(x)  # hello123