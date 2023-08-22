"""multiply all nos in a list using function"""
list=[1,2,3,4]
def list_mult(list):
    product=1
    for i in list:
        product=product*i
    return product

print("product is:",list_mult(list))

