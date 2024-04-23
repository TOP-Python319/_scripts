class Dog:
    pass


barky = Dog()

# breed
barky.breed = 'bullterier'
barky.age = 3

print(barky.age)

Dog.color = 'white'


print(Dog.__dict__)
print(barky.__dict__)
