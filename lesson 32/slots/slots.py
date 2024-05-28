from pprint import pprint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p = Point(1, 2)
p.z = 3

pprint(p.__dict__)


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p2 = PointSlots(3, 4)
p2.z = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'PointSlots' object has no attribute 'z'
pprint(p2.__dict__)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'PointSlots' object has no attribute '__dict__'. Did you mean: '__dir__'?