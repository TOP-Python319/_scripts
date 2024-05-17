# именование: в коцне класса принято писать Mixin. ClassMixin


class Mixin:
    def mixin_method(self):
        print('Это примесь!')


class MyClass(Mixin):
    def my_method(self):
        self.mixin_method()


o = MyClass()
o.my_method()