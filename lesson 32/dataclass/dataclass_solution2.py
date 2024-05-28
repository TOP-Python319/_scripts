from dataclasses import make_dataclass


Customer = make_dataclass('Customer', ('name', 'lastname', 'balance'))


c = Customer('Helen', 'Bonnem Carter', 1000)
d = Customer('Helen', 'Bonnem Carter', 1000)
print(c)

print(c == d)
