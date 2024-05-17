# защищённые методы и атрибуты
# перед названием ставится один знак подчёркивания
# работает на уровне соглашения
# на самом деле все защищённые атрибуты и методы доступны ото всюду

class BankAccount:
    
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_data(self):
        print(self._name, self._balance, self._passport)


acc1 = BankAccount('Serj', 1_000_000, 1001123456)
acc1.print_data()
print(acc1._name)
print(acc1._balance)
print(acc1._passport)

print(acc1.__dict__)