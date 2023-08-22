"""
Program to separate negative positive nos of a list
"""

A = [1,7,-8,6,-5,2,-4,0]
x=[]
y=[]

for i in A:
    if( i>=0):
        x.append(i)
        #print(x)
    
    else:
        y.append(i)
        #print(y)



print(A)
print(x)
print(y)


