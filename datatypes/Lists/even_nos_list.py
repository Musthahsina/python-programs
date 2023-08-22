"""
Write a python program to print all even numbers from a given list

"""

My_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=[]
for i in My_list:
    if(i%2==0):
        even.append(i)

print(even)
