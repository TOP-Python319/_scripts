# __abs__ определяет как будет вести себя объект, когда запрашивается абсодютное значение с помощью функции abs()

x = -32
y = 32

print(abs(x))
print(abs(y))


print(x.__abs__())
print(y.__abs__())
print('--------------------------')

class Distance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return abs(self.x - self.y)
    

d = Distance(4, -6)
print(abs(d))