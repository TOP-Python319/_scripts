# публичный доступ - все методы и атрибуты доступны
# название без модификаторов

class BankAccount:
    
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)


acc1 = BankAccount('Serj', 1_000_000, 1001123456)
acc1.print_data()
print(acc1.name)
print(acc1.balance)
print(acc1.passport)
print(acc1.__dict__)