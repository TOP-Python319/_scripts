class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('Get balance')
        return self.__balance

    def set_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def del_balance(self):
        print('Delete balance')
        del self.__balance

    # balance = property(
    #     fget=get_balance,
    #     fset=set_balance,
    #     fdel=delete_balance
    # )

    # balance = property(get_balance)
    # balance = balance.setter(set_balance)
    # balance = balance.deleter(del_balance)

    # get_balance = property(get_balance) декоратор не очень красивым способом


