def create_adder(x):
    def adder(y,z):
        return x+y+z
    return adder
print(create_adder(15)(10,50))