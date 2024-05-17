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
    
    @classmethod
    def m_to_km(cls, m):
        return m / 1000
    
    @classmethod
    def km_to_m(cls, km):
        return km * 1000
    
    @classmethod
    def m_to_mi(cls, m):
        return m / 1600
    
    @classmethod
    def mi_to_m(cls, mi):
        return mi * 1600
    
    @classmethod
    def km_to_mi(cls, km):
        return km / 1.6
    
    @classmethod
    def mi_to_km(cls, mi):
        return mi * 1.6
    
    @classmethod
    def format(cls, value, unit):
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

example = LengthConverter()
print(example.km_to_m(10))