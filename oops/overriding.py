class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print("I breath oxygen...")

    def food(self):
        print("I eat food...")


class Dog(Animal):
    def food(self):
        print("I eat food")  # overriding method


ob = Dog("Micky")
ob.food()
ob.breath()
