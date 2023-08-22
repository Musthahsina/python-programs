# def reverse(str):
#     str=str[::-1]
#     return str
# string='python'
# print(reverse(string))

'''
method1
'''

# def reverse(string):
#     s = list(string)
#     s.reverse()
#     print(''.join(s))
#
# string = 'python'
# reverse(string)

'''
method2
'''

# def reverse(string):
#     s=''
#     for i in string:
#         s=i+s
#         print(s)
# string='python'
# reverse(string)

'''
method3 ( listt comprehension)
'''
# str='python'
# string=[i for i in range(len(str)-1,-1,-1)]
# print(string)
# string=[str[i] for i in range(len(str)-1,-1,-1)]
# print(string)
# print(''.join(string))

# str='you are awesome'
# string=[i for i in range(len(str)-1,-1,-1)]
# string=[str[i] for i in range(len(str)-1,-1,-1)]
# print(''.join(string))

# string=input("enter the string:")
# def palindrome(string):
#     str=""
#     for i in string:
#         str=i+str
#     # print(str)
#
#     if str==string:
#          print("Plindrome")
#     else:
#          print("Not Palindrome")
#
# palindrome(string)

def reverse(string):
    string=[string[i] for i in range(len(string)-1,-1,-1)]
    # print(string)
    # print(s)
    x=''.join(string)
    if x==s:
        print("Palindrome")
    else:
        print("Not Palindrome")
        return x
s=input("Enter the string:")
print(reverse(s))
