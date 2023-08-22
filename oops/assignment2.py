"""1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the
class methods.
Hints:
Use __init__ method to construct some parameters"""


class StringUpper:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("enter the string:")

    def printString(self):
        print("string in uppercase:", self.string.upper())


# test function

def testStringUpper():
    upper = StringUpper()
    upper.getString()
    upper.printString()


testStringUpper()

"""Define a class with a generator which can iterate
the numbers, which are divisible by 7, between a
given range 0 and n.
(Just try )
Hints:
Consider use yield"""


# class DivisibleBySeven:
#     def __init__(self,num):
#         self.num=num
#
#     def iterate_the_numbers(self):
#         for i in range(self.num):
#             if i % 7 == 0:
#                 yield i
# div_nums=DivisibleBySeven(100)
# for div_nums in div_nums.iterate_the_numbers():
#     print(div_nums)

class DivisibleBySeven:
    def __init__(self, num):
        self.num = num

    def iterate_the_numbers(self):
        for i in range(self.num):
            if i % 7 == 0:
                print(i)


div_nums = DivisibleBySeven(100)
div_nums.iterate_the_numbers()

"""
3. Define a class, which have a class parameter and
have a same instance parameter.
Hints:
Define a instance parameter, need add it in
__init__ method
You can init a object with construct parameter
or set the value later
"""


class Class:
    cls_para = "Class parameter" #cls para=parameter before cons.

    def __init__(self, ins_para):
        self.ins_para = ins_para
    # def set_inspara(self,new_inspara):
    #     self.ins_para=new_inspara

ob1 = Class("instance parameter1")
print(ob1.ins_para)
print(ob1.cls_para)
print(Class.cls_para)
# ob1.set_inspara("New value")

"""
Define a class named American which has a
static method called printNationality.
Hints:
Use @staticmethod decorator to define class static
method.
"""


class American:
    @staticmethod
    def printNationality():
        print("American")


American.printNationality()

"""
Define a class named American and its subclass
NewYorker.
Hints:
Use class Subclass(ParentClass) to define a
subclass.
"""


class American:
    def __init__(self):
        print("American")


class Newyorker(American):
    def __init__(self):
        super().__init__()
        print("NewYorker")


alice = American()
ally = Newyorker()

"""
6. Define a class named Circle which can be
constructed by a radius. The Circle class has a
method which can compute the area.
Hints:
Use def methodName(self) to define a method.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = math.pi * self.radius ** 2
        return f"Area:{area}"


obj = Circle(6)
print(obj.getArea())

"""7. Define a class named Rectangle which can be
constructed by a length and width. The Rectangle
class has a method which can compute the area.
Hints:
Use def methodName(self) to define a method."""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        area = self.length * self.width
        return f"Area:{area}"


obj_rect = Rectangle(5, 6)
print(obj_rect.getArea())

"""
8. Define a class named Shape and its subclass
Square. The Square class has an init function
which takes a length as argument. Both classes
have a area function which can print the area of the
shape where Shape's area is 0 by default.
Hints:
To override a method in super class, we can define
a method with the same name in the super class.
"""


class Shape:
    def __init__(self):
        self.area = 0

    def getArea(self):
        print("Area of shape:", self.area)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def getArea(self):
        self.area = self.length ** 2
        print("Area of square", self.area)


ob_s = Shape()
ob_s.getArea()
ob_r = Square(5)
ob_r.getArea()

"""
Define a class Person and its two child classes:
Male and Female. All classes have a method
"getGender" which can print "Male" for Male class
and "Female" for Female class.
Hints:
Use Subclass(Parentclass) to define a child class.
"""


class Person:
    def getGender(self):
        pass


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


person = Person()
person.getGender()
male = Male()
male.getGender()
female = Female()
female.getGender()
