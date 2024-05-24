# В далекой-далекой галактике Федерация ведет ожесточенную войну с клингонами.
# Звездолеты Федерации оснащены мощными фазерами,
# а клингонские корабли – смертоносными фотонными торпедами.

# Обе стороны разработали усовершенствованные варп-двигатели для перемещения со
# сверхсветовой скоростью, и оборудовали свои корабли системами самоуничтожения на случай
# чрезвычайной ситуации.

# Для игры, посвященной этой войне, нужно создать абстрактный класс Starship с методами

# warp_speed(),
# fire_weapon(),
# self_destruct(). 

# Кроме того, нужно создать два подкласса 

# FederationStarship и KlingonWarship, 
# которые наследуют абстрактные методы Starship и реализуют свои собственные версии методов 
# warp_speed()
# fire_weapon()
# self_destruct().

from abc import ABC, abstractmethod


class Starship(ABC):

    @abstractmethod
    def warp_speed(self): ...
    @abstractmethod
    def fire_weapon(self): ...
    @abstractmethod
    def self_destruct(self): ...


class FederationStarship(Starship):

    def warp_speed(self):
        print('Включить варп-двигатели!')

    def fire_weapon(self):
        print('Выстрелить торпедами.')

    def self_destruct(self):
        print('Запускаю систему самоуничтожения.')


class KlingonWarship(Starship):

    def warp_speed(self):
        print('Включить варп-двигатели!')

    def fire_weapon(self):
        print('Выстрелить фазерами.')

    def self_destruct(self):
        print('Запускаю протокол самоуничтожения.')


enterprise = FederationStarship()
bird_of_prey = KlingonWarship()

enterprise.warp_speed()
bird_of_prey.warp_speed()

enterprise.fire_weapon()
bird_of_prey.fire_weapon()

enterprise.self_destruct()
bird_of_prey.self_destruct()
