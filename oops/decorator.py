"""
 a decorator is a design pattern or language feature that allows you to add extra functionality to an existing function or class without modifying its structure. Decorators provide a way to modify or enhance the behavior of functions or classes at runtime.

In many programming languages, including Python, decorators are implemented using special syntax and are denoted by
the @ symbol followed by the decorator name. They are typically applied to functions or classes, and they can wrap
the original function or class with additional code, modify the function's behavior, or provide some kind of
preprocessing or postprocessing.
"""


def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()

    return wrapper


@uppercase_decorator
def hello_name(name):
    return "hello " + name


print(hello_name("musthahsina"))


def deco_func(func):
    def wrapper():
        print("Before func execution")
        func()
        print("After function execution")

    return wrapper


@deco_func
def my_func():
    print("Inside my_func")


my_func()


def uppercase_decorator(func):
    def wrapper():
        result = func().upper()
        return result

    return wrapper


@uppercase_decorator
def say_hello():
    return "Hello, world!"


print(say_hello())

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result

    return wrapper


@timing_decorator
def heavy_computation(n):
    # Simulating a computationally intensive task
    result = sum(range(n))
    return result


# Usage:
print(heavy_computation(1000000))

"""
@classmethod
@staticmethod
"""

# Python program to demonstrate
# use of a class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls, x):
        print("Inside class_method")
        print("class_variable:", cls.class_variable)
        print("x:", x)

    @staticmethod
    def static_method(x):
        print("Inside static_method")
        print("x:", x)


# Calling the class method without creating an instance
MyClass.class_method(5)
# Output:
# Inside class_method
# class_variable: 10
# x: 5

# Calling the static method without creating an instance
MyClass.static_method(5)
# Output:
# Inside static_method
# x: 5

# Creating an instance of the class
obj = MyClass(20)

# Calling the class method through an instance
obj.class_method(8)
# Output:
# Inside class_method
# class_variable: 10
# x: 8

# Calling the static method through an instance
obj.static_method(8)


# Output:
# Inside static_method
# x: 8

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    @classmethod
    def create_square(cls, side):
        return cls(side, side)


# Creating an instance of the Rectangle class
rectangle = Rectangle(7, 6)
print(rectangle.area())
print(rectangle.perimeter())

# Creating a square using the class method
square = Rectangle.create_square(4)
print(square.area())
print(square.perimeter())


class BankAccount:
    interest_rate = 0.08

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        return self.balance * self.interest_rate

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        print("Interest rate updated using class method.")


# Creating an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing attributes and calling methods
print(account.account_number)
print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(200)
print(account.balance)

interest = account.calculate_interest()
print(interest)

# Using the class method to update the interest rate
BankAccount.set_interest_rate(0.1)
new_interest = account.calculate_interest()
print(new_interest)

"""
@staticmethod
"""


class Add_Mul:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b


# Calling the static methods
result1 = Add_Mul.add_numbers(5, 3)
print("Result of adding numbers:", result1)

result2 = Add_Mul.multiply_numbers(5, 3)
print("Result of multiplying numbers:", result2)


class Even:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


# Calling the static method
num1 = 4
is_even1 = Even.is_even(num1)
print(f"Is {num1} even? {is_even1}")

num2 = 7
is_even2 = Even.is_even(num2)
print(f"Is {num2} even? {is_even2}")
