class House:
    class Room:
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.rooms = [
            self.__class__.Room("Bedroom"),
            self.__class__.Room("Kitchen")
        ]


house = House()
