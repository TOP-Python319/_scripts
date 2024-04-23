class Animal:
    predatorFlag = True
    herbivoreFlag = True
    color = ''

    def __str__(self):
        return f'{self.color}, {self.predatorFlag}, {self.herbivoreFlag}'

lion = Animal()
lion.herbivoreFlag = False
lion.color = 'yellow'

goat = Animal()
goat.predatorFlag = False
goat.color = 'white'

print()
goat.sound = 'Me-e-e-e-e-eh!'

print(goat.__dict__)
print(goat)
print(lion.__dict__)
print(lion)
