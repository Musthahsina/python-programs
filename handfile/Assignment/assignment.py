# '''Number of lines in a file'''
#
# with open("myfile.txt", 'r') as file:
#     lines = len(file.readlines())
#     print('Total Number of lines:', lines)
#
# with open("myfile.txt", 'r') as file:
#     print("total lines=", len(file.readlines()))
#
# '''search for a string in text files'''
#
#
# with open('myfile.txt', 'r') as file:
#     # read all content from a file using read()
#     x = file.read()
#     # check if string present or not
#     str = input("enter the string:")
#     if str in x:
#         print('string exist')
#     else:
#         print('string does not exist')
#
# '''read specific lines from a file'''
# # method1
#
# with open('myfile.txt','r') as file:
#     s=''
#     x=file.readlines()[0:3]
# print(s.join(x))
#
# # method2
# import linecache
# line=linecache.getline("myfile.txt",1)
# print(line)
#
#
# '''reach each line in a file'''
#
# file = open('myfile.txt','r')
# for i in file:
#      print(i)
#
# '''
# total number of upper case letters in a file
# '''
#
# with open("myfile.txt", "r") as file:
#     data = file.read()
#     count_ucase = 0
#
# for ch in data:
#     if ch.isupper():
#         count_ucase += 1
#
# print("Total Number of Upper Case letters are:", count_ucase)
#
# '''append text to file'''
#
# with open("myfile.txt","a") as file:
#    file.write('helloo')
#    file.close()
#
# # with open("sample3.txt", "r") as fp:
# #     fp.truncate()


# lines = []
# # read file

# with open('myfile.txt', 'r') as fp:
#     # read an store all lines into list
#     lines = fp.readlines()
#     print(lines)
#
# with open('myfile.txt','w') as fp:
#     for number, line in enumerate(lines):
#             if number not in [1,2]:
#                 fp.write(line)
#

# with open('myfile.txt', 'r') as fp:
#     lines = fp.readlines()
#     print(lines)

# '''Writing List to a File in Python'''
#
# nuts = ['almond','cashew','walnut','hazelnut']
# with open('nuts.txt','w') as file:
#     for item in nuts:
#         file.write(item+"\n")
# file.close()

# names = ['1', '2', '3']
#
# with open('nuts.txt', 'w') as fp:
#     fp.write(','.join(names))

'''list,count files in directory
and  files with .txt'''
# import os
#
# list = os.listdir(r'C:\Users\USER\PycharmProjects\pythonProject1\handfile\Assignment')
# print("List of files :", list)
# count = 0
# for i in list:
#     count = count+1
# print("no: of files :", count)
# for i in list:
#     if i.endswith(".txt"):
#         print('Files with extension .txt :',i)

# '''Python Remove/Delete Non-Empty Folders'''
#
# import shutil
# shutil.rmtree(r'C:\Users\USER\PycharmProjects\pythonProject1\handfile\nefold')

# """ Python program to get file creation and modification date_time """
#
# import os.path, time
# newfile = open('new.txt','w')
# newfile.write("good morning")
# print("created time :", time.ctime(os.path.getctime('new.txt')))
# print("last modified time :", time.ctime(os.path.getmtime('new.txt')))

'''del lines'''

# import fileinput
# file='myfile.txt'
# linetodel=[1,2]
# def del_lines(file,linetodel):
#     with fileinput.input(file,inplace=True) as file:
#         for i in file:
#             if file.lineno() not in linetodel:
#                 print(i.rstrip())
#
# del_lines(file,linetodel)

import os
# dir_path=r'C:\Users\USER\PycharmProjects\pythonProject1\handfile\Assignment'
# def list_files()