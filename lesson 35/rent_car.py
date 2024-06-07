# Описание задачи:
# Создайте программу для управления парком автомобилей.
# В парке есть различные автомобили, каждый из которых имеет уникальные характеристики.

# Требования:
# 1. Создайте базовый класс для автомобилей и несколько подклассов для различных типов автомобилей 
#     (например, легковые и грузовые автомобили).
# 2. Реализуйте систему добавления автомобилей в парк и отображения информации о каждом автомобиле.
# 3. Реализуйте метод для аренды автомобилей и отслеживания их наличия.


class Car:
    def __init__(self, brand, model, year, gearbox, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.gearbox = gearbox
        self.price = price
        self.is_taken = False

    def take_car(self):
        if not self.is_taken:
            self.is_taken = True
            print(f'{self.brand} {self.model} {self.year} has been taken')
        else:
            print(f'{self.brand} {self.model} {self.year} is already taken')

    def return_car(self):
        if self.is_taken:
            self.is_taken = False
            print(f'{self.brand} {self.model} {self.year} has been returned')
        else:
            print(f'{self.brand} {self.model} {self.year} was not taken')


class Sedan(Car):
    def __init__(self, brand, model, year, gearbox, price, max_speed):
        self.max_speed = max_speed
        super().__init__(brand, model, year, gearbox, price)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.max_speed}'


class Wagon(Car):
    def __init__(self, brand, model, year, gearbox, price, seats):
        self.seats = seats
        super().__init__(brand, model, year, gearbox, price)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.seats}'


class Van(Car):
    def __init__(self, brand, model, year, gearbox, price, seats):
        self.seats = seats
        super().__init__(brand, model, year, gearbox, price)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.seats}'


class SUV(Car):
    def __init__(self, brand, model, year, gearbox, price, wheel_drive):
        self.wheel_drive = wheel_drive
        super().__init__(brand, model, year, gearbox, price)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.wheel_drive}'


class Park:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            status = 'taken' if car.is_taken else 'available'
            print(f'{car} — {status}')

    def take_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model and not car.is_taken:
                car.take_car()
                break
        else:
            print(f'Car {brand} {model} is not available.')

    def return_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model and car.is_taken:
                car.return_car()
                break
        else:
            print(f'Car {brand} {model} was not taken.')



# Пример использования
# rental = CarRental()

# sedan = Sedan("Toyota", "Camry", 2021, "15.1 cu ft")
# truck = Truck("Ford", "F-150", 2022, "3270 lbs")

# rental.add_car(sedan)
# rental.add_car(truck)

# rental.show_cars()
# rental.rent_car("Toyota", "Camry")
# rental.show_cars()
# rental.return_car("Toyota", "Camry")
# rental.show_cars()
# sedan = Sedan("Toyota", "Camry", 2022, 'AT', "100$", '220')

rental = Park()
sedan = Sedan("Toyota", "Camry", 2022, 'AT', "100$", '220')
sedan1 = Sedan("Toyota", "Camry", 2022, 'AT', "100$", '220')
sedan2 = Sedan("Toyota", "Camry", 2023, 'AT', "100$", '220')
sedan3 = Sedan("BMW", "3", 2023, 'AT', "100$", '220')
sedan4 = Sedan("Chevrolet", "Impala", 1970, 'MT', "100$", '280')
rental.add_car(sedan)
rental.add_car(sedan1)
rental.add_car(sedan2)
rental.add_car(sedan3)
rental.add_car(sedan4)
rental.show_cars()

rental.take_car('Toyota', 'Camry')
rental.take_car('Toyota', 'Camry')
rental.take_car('Toyota', 'Camry')