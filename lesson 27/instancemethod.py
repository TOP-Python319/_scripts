# Методы экземпляра
# Метода класса
# Статические методы


class Example:
    def hello():  
        print('hello')

    def instance_hello(self):
        print('instance hello')


Example.hello()
print(type(Example.hello))  # в данном случае hello() просто функция
# >>>: hello
# >>>: <class 'function'>

instance = Example()
print(type(instance.hello))  # в данном случае hello() метод экземпляра
# >>>: <class 'method'>
# instance.hello()
# >>>: TypeError: Example.hello() takes 0 positional arguments but 1 was given

instance.instance_hello()
# >>>: instance hello

Example.instance_hello()
# >>>: TypeError: Example.instance_hello() missing 1 required positional argument: 'self'