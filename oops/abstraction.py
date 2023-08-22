"""Abstraction is a fundamental principle in object-oriented programming (OOP) that allows you to represent complex
real-world entities as simplified models within your code. It involves hiding unnecessary details and exposing only
essential information and behavior relevant to the system being developed. Abstraction is achieved through abstract
classes and interfaces in Python."""

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


rectangle = Rectangle("Rectangle", 4, 6)
rectangle.print_details()

circle = Circle("Circle", 5)
circle.print_details()
