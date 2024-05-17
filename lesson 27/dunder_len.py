# __len__ определяет как будет вести себя объект, когда запрашивается длина с помощью функции len()
# __len__ должен возвращать целое не отрицательное число

tst_str = 'Hello wolrd!'
tst_lst = [1, 2, 3, 4, 5]
tst_dct = {'a': 2, 'c:': 3}

print(len(tst_str))
print(len(tst_lst))
print(len(tst_dct))

print(tst_str.__len__())
print(tst_lst.__len__())
print(tst_dct.__len__())

# print(len(32))
# >>>: TypeError: object of type 'int' has no len()
print('-------------------------------------')


class Person:
    def __init__(self, first_name, last_name=None, patronimus=None, matronimus=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.patronimus = patronimus
        self.matronimus = matronimus

    def __len__(self) -> int:
        return bool(self.first_name) + bool(self.last_name) + bool(self.patronimus) + bool(self.matronimus) 


dude = Person('Ivan', 'Ivanov')
print(len(dude))

soccer = Person('Криштиану', 'Роналду', 'душ Сантуш', 'Авейру')
print(len(soccer))

singer = Person('Bjork')
print(len(singer))