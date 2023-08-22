"""
constructor
"""


# parameterized cons.

class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Myclass("musthahsina", 26)  # creating an object
print(obj.name, obj.age)


# default cons.

class Myclass:
    name = "musthahsina"

    def __init__(self):
        pass


obj = Myclass()  # creating an object without passing parameters
print(obj.name)


class Myclass:
    def __init__(self):
        self.name = "musthahsina"
        self.age = 26


obj = Myclass()
print(obj.name)
