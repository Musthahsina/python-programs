# from functools import reduce
#
#
# def sum(a,b):
#     c=a+b
#     print(c)
# sum(10,4)
#
# num1=[1,2,3]
# num2=[4,5,6]
#
# result = map(lambda x,y: x*y,num1,num2)
# print(list(result))
#
# nums=[1,5,3,4]
# res = map(lambda x:x*x,nums)
# print(list(res))
#
# sqr=[i**2 for i in nums]
# print(sqr)
#
# res = map(lambda x:x**2,nums)
# print(list(res))
#
# """filter"""
# numbers=[-3,-6,-5,2,5,6,-2]
# less_than_zero=list(filter(lambda  x:x<0,numbers))
# print(less_than_zero)
#
# """matrix transpose"""
#
# # matrix=[[1,2],[3,4]
#
# list1=[1,5,4,6]
# product = reduce(lambda x,y:x*y,list1)
# print(product)
#
#
# marks=[78,88,80,34,56,97,91]
# less_than_eighty=list(filter(lambda  x:x<80,marks))
# print(less_than_eighty)
#

def cap(**kwargs):
    for key,value in kwargs.items():
        if isinstance(value,str):
            kwargs[key]=value.capitalize()
    print(kwargs)
cap(name='musthahsina',course='python')

# def cases(s):
#     return str(s).upper()
# char = {'a', 'b', 'f',  'i', 'o',}
# print("Characters:", char)
# result = map(cases, char)
# print("\nupper letters:")
# print(set(result))
