# ключевое понятие в ООП — объект.

# объект это контейнер:
# 1. данных, обозначающих текущее состояние контейнера
# 2. поведения


my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
print(my_list)
my_list.reverse()
print(my_list)
print()

# следующее ключевое понятие класс:
# класс объекта это коллекция характеристик, объединяющая атрибуты, имеющиеся у всех экземпляров подобного класса


# каждое значение в Python это объект. Каждый объект принадлежит к определённому классу.
print(type('Hello world!'))
print(type(5))
print(type(None))
print(type(lambda x: x**2))
print()

# isinstance()
x = 5
print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(x, bool))
s = 'simple string'
print(isinstance(s, int))
print(isinstance(s, str))
print(isinstance(s, float))

print(isinstance(my_list, object))
print(isinstance(x, object))
print(isinstance(s, object))



