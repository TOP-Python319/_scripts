# класс Student

# методы: 
#   конструктор, который принимает имя, фамилию, специальность (все приватные)
#   приватный метод, который выводит инфо о студенте
#   метод, который вызывает приватный метод


class Student:

    def __init__(self, name, lastname, speciality):
        self.__name = name
        self.__lastname = lastname
        self.__speciality = speciality


    def __print_info(self):
        print(f'Имя: {self.__name}')
        print(f'Фамилия: {self.__lastname[0]}.')
        print(f'Специальность: {self.__speciality}')

    def access_to_private_method(self):
        self.__print_info()


s1 = Student('Ivan', 'Gavrilov', 'artist')
s1.access_to_private_method()