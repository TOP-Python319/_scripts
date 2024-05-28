class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)

p2 = PointSlots(3, 4)


print('Без __slots__', p1.__dict__.__sizeof__(), p1.__sizeof__())
print('С __slots__', p2.__sizeof__())
