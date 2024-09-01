from abc import abstractmethod
from math import pi

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return round(self.base * self.height * 0.5, 2)

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 10)]

for shape in shapes:
    print(f"{shape.area()}cm²")