# на самом деле даже к приватным методам можно обратиться через конструкцию
# ЭК._НазваниеКласса__имяметода


class BankAccount:
    
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data(self):
        print(
            self.__name,
            self.__balance,
            f'{str(self.__passport)[:4]}******'
        )


acc1 = BankAccount('Serj', 1_000_000, 1001123456)
acc1.print_data()
# print(acc1.__name)
# print(acc1.__balance)
# print(acc1.__passport)
# print(acc1.__dict__)
# >>>: {'_BankAccount__name': 'Serj', '_BankAccount__balance': 1000000, '_BankAccount__passport': 1001123456}

print(acc1._BankAccount__name)
print(acc1._BankAccount__balance)
print(acc1._BankAccount__passport)



