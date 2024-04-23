class Person:
    name = 'Ivan'
    age = 30


man = Person()  # в переменной man хранится экземпляр класса Person

print(man.name)
print(man.age)

man.salary = 10000  # создаём атрибут salary для экземпляра man
print(man.salary)

man.salary = 1000  # изменяем атрибут salary для экземпляра man
print(man.salary)

delattr(man, 'salary')  # удаляем атрибут salary для экземпляра man
print(hasattr(man, 'salary'))