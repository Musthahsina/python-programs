#impotr math package to use math.pi for the value of PI
import math
#take radius of the   sphere from user
r=float(input("Enter the radius of a sphere:"))
#calculate the surface area of sphere
s_area=4*math.pi*pow(r,2)
#calculate the volume of sphere
volume=(4/3)*math.pi*pow(r,3)
#now printing the output
print("surface area of the sphere wll be %.2f" %s_area)
print("volume of the sphere will be  %.2f" %volume)

''''''

