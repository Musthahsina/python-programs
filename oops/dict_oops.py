class Animal:
    def __init__(self, identity, age):
        self.identity = identity
        self.age = age

    def feature(self):
        if self.age == '10':
            return True
        else:
            return False


ac = Animal('Lion', '10')
print(ac.__dict__)


"""__str__"""

"""Create a class Teacher with name, age, and salary attributes, where salary must be a private attribute that cannot 
be accessed outside the class."""

class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary

    def details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.__salary)

ob=Teacher('Musthahsina',26,20000)
ob.details()
# print(ob.__salary) wii show error
print(ob.name)