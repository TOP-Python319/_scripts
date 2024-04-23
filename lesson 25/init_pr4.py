# класс Person

# методы:

#+ конструктор, с именем, фамилией и возрастом

#+ метод возвращающий строку с Ф И

# метод, который возвращает True,
# в случае если человек старше 18 и False в противном случае


class Person:

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __str__(self):
        return f'Фамилия: {self.second_name}\nИмя:{self.first_name}\n'
    
    def is_adult(self) -> bool:
        if self.age < 18:
            return False
        return True
    
    
nina = Person('Нина', 'Такидзе', 40)
print(nina)
print('Взрослый' if nina.is_adult() else 'Не совершеннолетний')

