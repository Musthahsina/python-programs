"""
program to find largest no in a given list
My_list= [1,2,8,3,4,5]

"""

My_list = [1,2,8,3,4,5]

#My_list.sort()
#print("Largest no is:",My_list[-1])

#My_list.sort(reverse=True)
#print("Largest no is:",My_list[-1])


max = My_list[0]

for i in My_list:
    if i > max:
        max = i

print(max)

#smallest no in list
#
# min = My_list[0]
#
# for i in My_list:
#     if i < min:
#         min = i
# print(min)
#
#
# name="muthu"
# for i in name:
#     print(i)

