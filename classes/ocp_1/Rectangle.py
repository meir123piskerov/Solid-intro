
from classes.ocp_1.Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


a = Rectangle(4, 5)
print(a.area())
