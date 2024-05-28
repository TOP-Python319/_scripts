class SalaryNotInRangeError(Exception):
    """Исключение возникает из-за ошибок в зарплате

    Attributes:
        salary -- входная зарплата, которая выходит за допустимые пределы
        message -- объяснение ошибки
    """

    def __init__(self, salary, message="Зарплата не входит в диапазон от 0 до 50000"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    # переопределяем метод __str__
    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input('Введите зарплату: '))
if not 0 <= salary <= 50000:
    raise SalaryNotInRangeError(salary)