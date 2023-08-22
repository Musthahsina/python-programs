"""
Tuple
______

indexed,ordered,immutable



thistuple = ("apple",89,6,"banana","apple",)
print(thistuple)

print(thistuple[0])
print(thistuple[-1:])
print(thistuple[:-1])
print(thistuple[1:])
print(thistuple[1:-1])
print(thistuple[::-1])
print(thistuple[1::])
"""
thistuple = ("apple",89,6,"banana","apple",[8,"rtyu",0])
y=list(thistuple)
y[0]="grapes"
print(y)
print(tuple(y))

y=("orange",)
thistuple += y
print(thistuple)

print(thistuple[3][0])
print(thistuple[5][0])
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(y)

