from typing import Protocol


class Animal(Protocol):
    def make_sound(self) -> None: ...
    def walk(self) -> None: ...


class Dog:
    def make_sound(self) -> None:
        print('bark')

    def walk(self) -> None:
        print('walk')


def make_animal_sound(animal: Animal) -> None:
    animal.make_sound()


d = Dog()
make_animal_sound(animal=d)

