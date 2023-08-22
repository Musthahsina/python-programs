"""
 Write a python program to remove repeated elements from a given list without using built-in methods
        list_to_remove = ["let's","google","the","pineapple","photo","google","photo",""]


"""

list_to_remove = ["let's", "google", "the", "pineapple", "photo", "google", "photo", ""]

removed_list = []

for i in list_to_remove:
   if i not in removed_list:
       removed_list.append(i)

print(removed_list)



# str="Let's google the pineapple"
# print(str)
# str1=str.split()
# print(str1)
#
# for i in str1:
#     l=""