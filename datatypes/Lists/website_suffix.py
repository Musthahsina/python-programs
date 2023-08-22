"""
["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
Write a python program to print website suffixes (com , org , net ,in) from this list.

"""

L1= ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
L2=[]
for i in L1:
    suffix = i.split(".")[-1]
    L2.append(suffix)
print(L2)

