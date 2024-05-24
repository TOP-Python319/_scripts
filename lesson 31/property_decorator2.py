class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # геттер для атрибута __balance
    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance

    # сеттер для атрибута __balance
    @my_balance.setter
    def my_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    # делитер для атрибута __balance
    @my_balance.deleter
    def my_balance(self):
        print('Delete balance')
        del self.__balance


x = BankAccount('Paul', 100)
x.my_balance
# Get balance
# 100
x.my_balance = 'asdasd'
# Set balance
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/maks/Work/top-academy/python 319/.scripts/lesson 31/property_decorator2.py", line 17, in my_balance
#     raise ValueError('Баланс должен быть числом')
# ValueError: Баланс должен быть числом
x.my_balance = 1.1
# Set balance
x.my_balance
# Get balance
# 1.1