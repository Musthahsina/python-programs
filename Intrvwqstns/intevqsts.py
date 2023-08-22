# """"2---"""
#
# str1 = "Let's google the pineapple photo "
# x = str1.split()
# rev1 = []
# for i in x:
#     rev1.append(i[::-1])
#     rev2 = " ".join(rev1)
# print(rev2)
#
# """4--------"""
#
# s= "1982376455"
# odd=[]
# even=[]
# x=list(s)
# for i in x:
#     if int(i)%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# odd.sort()
# even.sort(reverse=True)
# a=odd+even
# print(a)
# b=''.join(a)
# print(b)
#
# """"7-----"""
# #
# # num=ord("B")-ord("A")
# # for i in range(num,ord("e")):
# #     print(i,end=' ')
#
# """10"""""
# n='123'
# num=0
# l=len(n)
# for i in n:
#     num=(num*10)+(ord(i)-48)
# print(num)
#
# """5"""
# l=[34,87,90,80,25]
# print(l)
# min=l[0]
# max=l[0]
# print(len(l))
# for i in range(len(l)):
#     if l[i]>=max:
#         max=l[i]
#     if l[i]<=min:
#         min=l[i]
# print("Maximum value:",max)
# print("Minimum value:",min)

#3
#
# d1={"name":"priya","place":"priya","qual":"btech","age":"26"}
# d1=dict.fromkeys("priya")
# print(d1)
# # print(d1["place"])
