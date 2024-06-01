from typing import List


class Wheel:
    def __init__(self, position):
        self.position = position


class Car:
    def __init__(self):
        self.wheels: List[Wheel] = [
            Wheel("front left"),
            Wheel("front right"),
            Wheel("rear left"),
            Wheel("rear right")
        ]


car = Car()
