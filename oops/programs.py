'''Create a class called Vehicle with the following attributes and methods:

Attributes:
make: a string representing the make of the vehicle
model: a string representing the model of the vehicle
year: an integer representing the year the vehicle was made
color: a string representing the color of the vehicle
mileage: a float representing the current mileage of the vehicle

Methods:
_init_(self, make, model, year, color, mileage): initializes the attributes with the given values
drive(self, distance): takes a float representing the distance driven and updates the mileage attribute accordingly
get_info(self): returns a string with the vehicle's make, model, year, color, and mileage attributes in a formatted way
Create a subclass called Car that inherits from the Vehicle class with the following additional attributes and methods:
Attributes:
num_doors: an integer representing the number of doors the car has
engine_type: a string representing the type of engine the car has
Methods:
_init_(self, make, model, year, color, mileage, num_doors, engine_type): initializes the attributes with the given values
get_info(self): overrides the get_info method of the Vehicle class to include the num_doors and engine_type attributes
Create an instance of the Vehicle class and call the drive method with a distance of 100. Then call the get_info method
to print out the vehicle's information.

Create an instance of the Car class and call the drive method with a distance of 50. Then call the get_info method to
print out the car's information.
"""

"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in init method
    You can init a object with construct parameter or set the value later
'''


class Vehicle:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance  # updates the mileage according the distance
        # mileage is the distance the car has already traveled.
        # distance is distance driven

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Mileage: {self.mileage}"
        # print(self.make, self.model, self.year, self.color, self.mileage)


class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage, num_doors, engine_type):
        # using super() to access and invoke methods and properties defined in the superclass Vehicle
        super().__init__(make, model, year, color, mileage)
        self.num_doors = num_doors
        self.engine_type = engine_type

    def get_info(self):
        vehicle_info = super().get_info()
        return f"{vehicle_info}, Number of Doors: {self.num_doors}, Engine Type: {self.engine_type}"


# An instance of the Vehicle class.
vehicle = Vehicle("Toyota", "Camry", 2022, "Silver", 500.2)
vehicle.drive(100)
print(vehicle.get_info())

# An instance of the Car class.
car = Car("Honda", "Civic", 2021, "Black", 700.6, 4, "Petrol")
car.drive(50)
print(car.get_info())

''''''


class Person:
    name = "The person is:"  # class parameter

    def __init__(self, age):
        self.age = age  # "instance parameter"


# Creating objects and accessing parameters
obj1 = Person("Musthahsina")
print("%s Course is %s" % (Person.name,Person.name))
obj2 = Person("XYZ")

# print(obj1.course)
# # print(Person.course)
# print(obj1.name)
#
# print(obj2.course)
# print(obj2.name)
