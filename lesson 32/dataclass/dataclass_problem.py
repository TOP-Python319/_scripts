class Customer:

    def __init__(self, name, lastname, balance):
        self.name = name
        self.lastname = lastname
        self.balance = balance

    def __str__(self):
        return f'Customer {self.name} {self.lastname}, {self.balance}'


c = Customer('Helen', 'Bonnem Carter', 1000)
print(c)
