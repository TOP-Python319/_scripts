# ТАК ДЕЛАТЬ НЕ НАДО
# нарушает соглашение
# замедляет код


from accessify import protected, private


class Car:

    @private
    def start_engine(self):
        return "Engine's sound."

    def run(self):
        return self.start_engine()


car = Car()

print(car.run())
# print(car.start_engine())
# print(dir(car))
