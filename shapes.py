import math

class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Examples:
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(8, 10, 6, 7, 8)

print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())

print("Triangle - Area:", triangle.calculate_area())
print("Triangle - Perimeter:", triangle.calculate_perimeter())
