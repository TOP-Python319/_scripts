class Car:
    def __init__(self, make, model):
        self.make = make
        self.maker = model

    def display_info(self):
        return f"{self.make} {self.model}"

car = Car("Toyota", "Camry")
print(car.display_info())


# AttributeError: 'Car' object has no attribute 'model'