# класс LengthConverter

# методы:
#   m_to_km
#   km_to_m
#   m_to_mi
#   mi_to_m
#   km_to_mi
#   mi_to_km


class LengthConverter:

    METER = 'm'
    KILOMETER = 'km'
    MILE = 'mi'
    
    def __init__(self, attr):
        self.attr = attr

    @staticmethod
    def try_to_get_attr(self):
        print(self.attr)

    @staticmethod
    def m_to_km(m):
        return m / 1000
    
    @staticmethod
    def km_to_m(km):
        return km * 1000
    
    @staticmethod
    def m_to_mi(m):
        return m / 1600
    
    @staticmethod
    def mi_to_m(mi):
        return mi * 1600
    
    @staticmethod
    def km_to_mi(km):
        return km / 1.6
    
    @staticmethod
    def mi_to_km(mi):
        return mi * 1.6
    
    @staticmethod
    def format(value, unit):
        if unit == LengthConverter.METER:
            symbol = 'm'
        elif unit == LengthConverter.KILOMETER:
            symbol = 'km'
        elif unit == LengthConverter.MILE:
            symbol = 'mi'

        return f'{value} {symbol}.'
    

km = LengthConverter.m_to_km(3800)
print(km)

mi = LengthConverter.km_to_mi(72000)
print(LengthConverter.format(mi, LengthConverter.MILE))


# статический метод не может получить доступ к атрибутам ЭК, так как
# он не принимает self/cls
# static_instance = LengthConverter(attr='ПОПЫТКА')
# print(static_instance.try_to_get_attr())
# TypeError: LengthConverter.try_to_get_attr() missing 1 required positional argument: 'self'
