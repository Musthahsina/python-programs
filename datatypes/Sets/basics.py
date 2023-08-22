"""
1.unchangable,unordered,unindexed,duplicates not allowed
"""
# set1={"Musthahsina",12,"python","MCA",12,"python"}
# print(set1)
#
#
# x=list(set1)
# print(x)
# print(x[0])
#
#
# set2 = {"mango", "banana", "kiwi"}
# tropical ={"pineapple","papaya"}
#
# #add
#
# set2.add("apple")
#
# print(set2)
#
# #update
#
# set2.update(tropical)
# print(set2)
#
# #remove
#
# set2.remove("kiwi")
# print(set2)
#
# #discard
#
# set2.discard("banana")
# print(set2)

#pop
#
# x=set2.pop()
# print(x)
# print(set2)

#clear

# set2.clear()
# print(set2)

#del

#del set2
#print(set2)


#Loop items

# for x in set2:
#   print(x)
#
# copy

# set3=set2.copy()
# print(set3)
#
# set1={"Musthahsina",12,"python","MCA",12,"python",(1,2,3),}
# print(set1)
# s ={set[1,2,3,4]}
# print(type(s))

# A = {"musthahsina",12,"python","btech"}
# B = {"priya",12,"python","bca","python"}
#
# # print(A.union(B))
# # print(A.difference(B))
# # print(A.intersection(B))
# # print(A.symmetric_difference(B))
# # print(A.difference_update(B))
# # print(A.intersection_update(B))
# print(A.symmetric_difference_update(B))
# print(A)

# 1)write a program to find common number from 2  set
# a = {13,5,3,5,7}
# b = {3,5,4,7}
# print(a.intersection(b))

# 2)add an element to set S1 and remove an element from set S2
# S1 = {100, 120, 130, 140, 150}
# S2 = {120, 130, 140,150, 160, 170}
# S1.add(160)
# S2.remove(150)
# print(S1)
# print(S2)


# output ={20, 70, 10, 60}

# 3)update elements in set1 from set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.update(set2)
print(set1)
# output={20, 70, 10, 60}
#
#
#
#
#


