# абстракция это процесс выделения существенных харатеристик объекта и игнорирования несущественных деталей.
# абстракция используется для упрощения сложных задач и сокрытия деталей реализации.

# абстракция функций

def add_numbers(x: int, y: int) -> int:
    return x + y


# абстракция классов
class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def withdraw(self, amount: int):
        """Снять деньги"""
        ...

    def deposit(self, amount: int):
        """Внести деньги"""
        ...

    def get_balance(self) -> int:
        """Получить баланс"""
        ...
