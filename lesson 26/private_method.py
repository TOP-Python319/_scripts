# приватные методы и атрибуты
# перед названием ставится два знака подчёркивания

# не путать с магическим методом
# магический метод: __названиеметода__
# защищённый метод: _названиеметода
# приватный метод: __названиеметода

# сокрытие данных называется инкапсуляцией


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
print(acc1.__dict__)