from math import hypot

class Vector():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Vector (%r, %r)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __mul__(self, scalar):
        return Vector(self.a * scalar, self.b * scalar)

    def __abs__(self):
        return hypot(self.a, self.b)

    def __bool__(self):
        return bool(abs(self))

