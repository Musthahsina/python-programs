"""
 Write a python program to create a list of even numbers and another list of odd numbers from a given list

"""

My_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even=[]
odd=[]

for i in My_list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("Even List:",even)
print("Odd List:",odd)
