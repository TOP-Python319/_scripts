from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...


# s = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    

c = Circle(5)
print(c.area())
print(c.perimeter())
print('-' * 20)
r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())
print('-' * 20)
t = Triangle(3, 4, 5)
print(t.area())
print(t.perimeter())