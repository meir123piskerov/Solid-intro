
from classes.ocp_1.Shape import Shape


class Circle(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2
