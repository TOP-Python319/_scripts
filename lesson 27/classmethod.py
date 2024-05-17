# пример для классового метода (метода класса)
# class ClassName:
#     @classmethod
#     def class_method(cls, name):
#         pass


class Example:

    @classmethod
    def class_hello(cls):  # этот метод принимает значение класса в атрибут cls 
        print('hello')

# cls не зарезервированное, но общепринятое название, обозначающее название класса.
# используется когда мы хотим указать, что в данной месте будет применяться именно класс


Example.class_hello()
# >>>: hello

instance = Example()
instance.class_hello()
# >>>: hello    