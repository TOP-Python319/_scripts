# класс NewInt, унаследованный от int

# с дополнительными методами:
#     len - длина числа
#     isnegative - отрицательное число или нет
#     iseven - чётное число или нет


class NewInt(int):

    def isnegative(self):
        return self < 0

    def iseven(self):
        return self % 2 == 0

    def __len__(self):
        return len(str(self))

    def len(self):
        return self.__len__()


d = NewInt(65536)
print(d.len())
print(d.isnegative())
print(d.iseven())
print(len(d))
