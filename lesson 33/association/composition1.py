class Person:

    class Heart:
        def __init__(self):
            self.beats = 0

        def beat(self):
            self.beats += 1
            print(f"Heart beats: {self.beats}")

    def __init__(self, name):
        self.name = name
        self.heart = self.__class__.Heart()  # Композиция

    def live(self):
        print(f"{self.name} is living.")
        self.heart.beat()


# Создание объекта
person = Person("John")

# Человек живет, и его сердце бьется
person.live()
