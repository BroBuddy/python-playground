from math import pi

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def circumference(self):
        return round(pi * self.radius * self.radius, 2)
    
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def circumference(self):
        return round(self.width * self.width)
    
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

circle = Circle(color = "red", is_filled = True, radius=5)
square = Square(color = "blue", is_filled = False, width=10)

circle.describe()
print(f"{circle.circumference()}cm²")
print()

square.describe()
print(f"{square.circumference()}cm²")
print()