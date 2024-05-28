from enum import Enum


class ColorRGB(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


print(Day.MONDAY.name)
print(Day.MONDAY.value)


days_dict = {
    'MONDAY': 1,
    'TUESDAY': 2,
    'WEDNESDAY': 3,
    'THURSDAY': 4,
    'FRIDAY': 5,
    'SATURDAY': 6,
    'SUNDAY': 7
}

day_value = days_dict['MONDAY']  # Получение значения по ключу
