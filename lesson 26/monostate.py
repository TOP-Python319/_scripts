class Cat:

    def __init__(self, breed='', color=''):
        self.breed = breed
        self.color = color

tom = Cat('brit', 'grey')
scratch = Cat('garbage', 'black')

print(tom.__dict__)
print(scratch.__dict__)

tom.color = 'red'

print(tom.__dict__)
print(scratch.__dict__)


# паттерн моносостояние (monostate)
# паттерн Борг (Borg)
