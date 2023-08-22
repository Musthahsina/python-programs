"""
The circle class models a circle with a radius and color

attributes : radius , color

methods :

Circle
getRadius()
getCircumference()
getArea()
"""

import math


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def getCircumference(self):
        circumference = 2 * math.pi * self.radius
        return f"Circumference of the circle with radius {self.radius} and color {self.color} is: {circumference}"

    def getArea(self):
        area = math.pi * self.radius ** 2
        return f"Area of the circle with radius {self.radius} and color {self.color} is:{area}"


ob_circle = Circle(9, "yellow")
print(ob_circle.getRadius())
print(ob_circle.color)
print(ob_circle.getCircumference())
print(ob_circle.getArea())
