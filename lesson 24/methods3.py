class Car:
    color = 'red'
    engine = 4.0

    # параметр self передается первым при вызове метода
    # назвать параметр можно как угодно, но по PEP8 принято называеть его self
    def drive(self):
        print(f'!!!drive {self}!!!')


nissan = Car()
toyota = Car()


# метод класса должен получить параметр self
# а именно какой-то экземпляр класса Car
# Car.drive()
# >>>: TypeError: Car.drive() missing 1 required positional argument: 'self'


Car.drive(nissan)
Car.drive(toyota)

# Car.drive(nissan) по сути эквивалент nissan.drive()