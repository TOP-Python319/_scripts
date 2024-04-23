# класс Counter,
# экземпляры класса, будут считать внутри себя значения

# атрибут value

# методы:
# start - значение с которого начинаем считать, по умолчанию 0
# increment - метод, который увеличивает значение на 1
# display - метод, который печатает значение value
# reset - обнуляет счётчик


class Counter:

    def start(self, value=0):
        self.value = value

    def increment(self, inc=1):
        self.value += inc

    def display(self):
        print(f'{self} = {self.value}')

    def reset(self):
        # self.value = 0
        self.start()

    # статический метод работает с БАЗОВЫМ КЛАССОМ, а не с ЭК
    @staticmethod
    def test_static_method():
        print('Это статический метод')


x = Counter()
y = Counter()
x.start()  # value = 0
y.start(100)
x.increment()  # value = 1
x.increment()  # value = 2
x.increment()  # value = 3
x.increment()  # value = 4
x.increment()  # value = 5
x.increment()  # value = 6
y.increment(1000), y.increment(), y.increment(), y.increment(), y.increment()
x.display() # получаем значение value, то есть 6
x.reset()  # value = 0
x.display() # получаем значение value, то есть 0
y.display()