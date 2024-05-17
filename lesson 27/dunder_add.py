# __add__ определет операцию сложения при помощи +


s = 'Hello'
w = 'World'
print(s + w)
print(s.__add__(w))
print(w + s)
print(w.__add__(s))

x = 5
y = 10
print(x + y)
print(x.__add__(y))
print(y + x)
print(y.__add__(x))

print('--------------------------')


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance


a = BankAccount('Ivan', 100)
b = BankAccount('Petr', 200)
print(a + 500.5)
print(300.5 + a)
print(a + b)
print(b + a + 10 + a)

a = a + 10
a += 10
print(a)



