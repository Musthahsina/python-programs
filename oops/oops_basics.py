# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         print("The car engine is started.")
#
#     def stop_engine(self):
#         print("The car engine is stopped.")
#
# # Creating objects of the Car class
# car1 = Car("Toyota", "Camry", 2022)
# car2 = Car("Ford", "Mustang", 2021)
#
# # Accessing object properties
# print(car1.make)  # Output: Toyota
# print(car2.model)  # Output: Mustang
#
# # Invoking object methods
# car1.start_engine()  # Output: The car engine is started.
# car2.stop_engine()  # Output: The car engine is stopped.

''' def ___init___(self)  #constructor '''

#
# class Car:
#     def __init__(self, car_name, model, year):
#         self.car_name = car_name
#         self.model = model
#         self.year = year
#     def drive(self):
#         print("Driving",self.car_name,self.model)
#     def stop(self):
#         print("car is stopped",self.car_name,self.model)
#
# obj = Car("maruti suzuki", "alto", 2000)
# print(obj.year)
# print(obj.model)
# obj.drive()
# obj.stop()
'''--oops---

1.class - its a collection of objects

2.objects - instances of class

3.inheritance - Inheritance allows creating new classes 
                (derived or child classes) based on existing classes 
                (base or parent classes). The child classes inherit the
                properties and methods of the parent class,
                enabling code reuse and creating an "is-a" r
                elationship between classes.Inheritance supports hierarchical 
                classification and promotes modularity.
                
4.polymorphism -  Polymorphism refers to the ability of objects of different 
                  classes to respond differently to the same message
                  or method call. It allows objects to be treated as instances 
                  of their own class or as instances of their parent 
                  class. Polymorphism enables flexibility and 
                  extensibility in design by providing a common
                  interface for multiple related classes.

5.encapsulation - Encapsulation is the principle of 
                  bundling data and methods together within a class, 
                  hiding the internal details and exposing only necessary 
                  interfaces to interact with the object. It helps in 
                  achieving data abstraction and protects data
                  from unauthorized access or modification.

6.abstarction - Abstraction focuses on representing essential 
            features and behaviors of an object while hiding 
            unnecessary implementation details. It allows the 
            creation of abstract classes or interfaces that 
            define common attributes and methods without providing
            a specific implementation. Abstraction helps in
            designing modular and loosely coupled systems.


'''

'''
inheritance
---------------

Types:

1.Single inheritance
2.Multiple inheritance
3.Multilevel inheritance
4.Hierarchical inheritance
5.Hybrid inheritance


'''

# class Animal:  # parent class
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
#
#     def test(self):
#         print("parent class")
#
#
# class Dog(Animal):  # child class
#     def speak(self):
#         print("dog name is", self.name, self.category)
#
#
# class Cat(Animal):  # child class
#     def speak(self):
#         print("cat name is", self.name, self.category)
#
#
# obj_dog = Dog("micky", "pet")
# obj_dog.test()
# obj_dog.speak()
# obj_cat = Cat("kitty","pet")
# obj_cat.speak()

'''
Multiple inheritance - One child can inherit from multiple parent classes.

'''

#
# class Vehicle:  # parent class1
#     def vehicle_info(self):
#         print('Inside Vehicle class')
#
#
# class Car:  # parent class2
#     def car_info(self):
#         print('Inside Car class')
#
#
# # child class
#
# class Sportscar(Car, Vehicle):
#     def sports_car_info(self):
#         print('Inside Sports car class')


'''
Multilevel inheritance - a class can inherit properties and methods from a parent class, which in turn can be inherited by its own child class. This creates a hierarchical structure of classes with multiple levels of inheritance.

A->B->C  (B inherits from A, C from B.
'''

#
# class Vehicle:  # parent class1
#     def vehicle_info(self):
#         print('Inside Vehicle class')
#
#
# class Car(Vehicle):  # child class
#     def car_info(self):
#         print('Inside Car class')
#
#
# class Sportscar(Car):
#     def sports_car_info(self):
#         print('Inside Sports car class')
#
#
# vehicle = Vehicle()
# vehicle.vehicle_info()
#
# car = Car()
# car.car_info()
# car.vehicle_info()
#
# sport = Sportscar()
# sport.car_info()
# sport.vehicle_info()
# sport.sports_car_info()

'''
Hierarchical inheritance

'''
class Vehicle:
    def info(self):
        print('This is vehicle')


class Car(Vehicle):
    def car_info(self, name):
        print('car name is', name)


class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is', name)

# obj1 = Car()
# obj1.car_info('BMW')
# obj1.info()

obj2 = Truck()
obj2.info()


'''
Hybrid-combination of different inheritance
'''


class Vehicle:
    def info(self):
        print('This is vehicle')


class Car(Vehicle):
    def car_info(self, name):
        print('car name is', name)


class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is', name)

class Sportscar(Car, Truck):
    def sports_car_info(self):
        print('inside the sports car class')

s_car = Sportscar()
s_car.truck_info('TATA')
s_car.car_info('alto')
s_car.info()


