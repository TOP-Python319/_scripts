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

    # статический метод работает и с БАЗОВЫМ КЛАССОМ и с ЭК
    @staticmethod
    def test_static_method():
        print('Это статический метод')


x = Counter()
y = Counter()
x.test_static_method()
Counter.test_static_method()


# class Maths:
#     @staticmethod
#     def sum():
#         pass
    
#     @staticmethod
#     def mult():
#         pass

#     @staticmethod
#     def div():
#         pass