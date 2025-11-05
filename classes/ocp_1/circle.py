
from classes.ocp_1.Shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, r):

        self.r = r


    def area(self):
        radius = (self.r ** 2) * pi
        return radius


a = Circle(5)
print(a.area())
