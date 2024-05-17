class NewList(list):
    
    def delete(self, index=-1):
        del self[index]


x = NewList()
x.append(1)
x.append(2)
x.append(3)
print(x)

x.reverse()
print(x)

print(type(x))

print(isinstance(x, list))
print(isinstance(x, NewList))
print(isinstance(x, object))

x.delete()
print(x)

x.delete(0)
print(x)
