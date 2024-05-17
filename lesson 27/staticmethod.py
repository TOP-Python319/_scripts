# статический метод отвязан и от ЭК и от самого класса

class Example:

    @staticmethod
    def static_hello():  # этот метод не принимает никаких аргументов, ни сам класс, ни ЭК
        print('static hello')

Example.static_hello()
instance = Example()
instance.static_hello()