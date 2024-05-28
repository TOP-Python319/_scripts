# dataclass реализует __init__, __repr__, __str__, __eq__


from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    lastname: str
    balance: int

    def name_lastname(self):
        print(self.name + ' ' + self.lastname)


c = Customer('Helen', 'Bonnem Carter', 1000)
d = Customer('Helen', 'Bonnem Carter', 1000)
print(c)
c.name_lastname()

print(c == d)
