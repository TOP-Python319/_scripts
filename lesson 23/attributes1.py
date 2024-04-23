class Car:
    """Класс для определения характеристик машины"""
    color = 'red'
    engine = 1.8
    gearbox = 'AT'

toyota = Car()
nissan = Car()

print('Toyota: ', toyota.color)  # red
print('Toyota: ', toyota.engine)  # 1.8
print('Toyota: ', toyota.gearbox)  # AT
print('Toyota id: ', id(toyota))
print()

print('Nissan: ', nissan.color) # red
print('Nissan: ', nissan.engine) # 1.8
print('Nissan: ', nissan.gearbox) # AT
print('Nissan id: ', id(nissan))
print()

nissan.color = 'blue'
nissan.engine = 2.8
nissan.gearbox = 'MT'

print('Toyota: ', toyota.color)  # red
print('Toyota: ', toyota.engine)  # 1.8
print('Toyota: ', toyota.gearbox)  # AT
print('Toyota id: ', id(toyota))
print()

print('Nissan:', nissan.color)  # blue
print('Nissan:', nissan.engine)  # 2.8
print('Nissan:', nissan.gearbox)  # MT
print('Nissan id: ', id(nissan))