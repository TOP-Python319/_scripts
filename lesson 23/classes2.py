# class <название класса>:
#     <тело класса>

# pep8
# классы пишутся с большой буквы оформляются по типу написания CamelCase

# CamelCase - имена классов
# snake_case - имена переменных и функций
# kebab-case - в python не используется
# lowerCamelCase - в python не используется
# CAPS_LOCK - помечаются имена констант

class Car:
    """Класс для определения характеристик машины"""
    pass

# метод __doc__  
print(Car.__doc__)

# на основе класса мы можем создавать экземпляры класса (ЭК)
# ЭК - объекты созданные по определению класса
# чтобы создать ЭК нужно вызвать класс
# результат вызова класса - ЭК, который мы можем сохранить в переменную

nissan = Car()
toyota = Car()

print(type(nissan))
print(type(toyota))
print(isinstance(nissan, Car))
print(isinstance(toyota, Car))

print(id(nissan))
print(id(toyota))
