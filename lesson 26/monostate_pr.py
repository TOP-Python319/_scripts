# класс FireAlarm
# атрибуты:
#     когда меняли батарейку
#     когда была последняя пожарная проверка
#     фирма-производитель
# методы: 
#   update_data, который изменяет состояние сразу трёх показателей
#   get_data, который вызывает кортеж этих трёх показателей

# в базовом виде шаблон Моносостояние выглядит так:
# в базовом классе создаётся словарь
# который перезаписывает хранилище атрибутов (__dict__) у 
# каждого экземпляра класса

# class ClassName:
#     __shared_attributes = {}

#     def __init__(self):
#         self.__dict__ = ClassName.__shared_attributes

class FireAlarm:
    __shared_attributes = {
        'last_battery_swap': '',
        'last_fireguard_inspection': '',
        'brand': '',
    }

    def __init__(self):
        self.__dict__ = FireAlarm.__shared_attributes

    def update_data(self, swap_date, inspection_date, brand):
        self.last_battery_swap = swap_date
        self.last_fireguard_inspection = inspection_date
        self.brand = brand

    def get_data(self):
        return tuple(self.__shared_attributes.values())


sensor1 = FireAlarm()
sensor2 = FireAlarm()
sensor1.brand = 'Fujitsu'
print(sensor1.__dict__)
print(sensor2.__dict__)
print('---------------------')
sensor3 = FireAlarm()
sensor3.last_battery_swap = '26.04.2024'
sensor3.last_fireguard_inspection = '26.04.2024'
print(sensor1.__dict__)
print(sensor2.__dict__)
print(sensor3.__dict__)
print('---------------------')
sensor1.update_data('01.01.1970', '01.01.1970', 'JVC')
print(sensor1.__dict__)
print(sensor2.__dict__)
print(sensor3.__dict__)
print('---------------------')
print(sensor3.get_data())
