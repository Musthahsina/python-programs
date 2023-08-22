"""

Write a python program to find the common numbers from two lists

"""

List_one = [1, 2, 3, 4, 5, 8]
List_two = [3, 4, 5, 6, 7, 8]
common=[]

#for i in List_one:
 #   if i in List_two:
  #      common.append(i)
#print(common)


for i in List_one:
    for j in List_two:
        if(i==j):
            common.append(i)

print(common)
