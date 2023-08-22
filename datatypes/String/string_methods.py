"""
upper
lower
capitalize
find
join
split
"""



str1="Hello world"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.find("h"))
list=['apple','orange','mango']
x= ''.join(list)
print(x)
print(str1.split("llo"))


#islower
txt="musthahsina"
y = txt.islower()
print(y)
y=txt.isupper()
print(y)
y=txt.isdigit()
print(y)
print(len(txt))

"""
append mew string 

s1 = "Python"
s2 = "Luminar"

"""

s1 = "Python"
s2 = "Luminar"
mid = int(len(s1)/2)
print(mid)
x=s1[:mid:]
print(x)
x=x+s2
print(x)
y=s1[mid:]
x=x+y
print(x)

"""
create a new string made of the first,middle,and last characters of each input string

s1 = "Python"
s2 = "Luminar"

0/p: PLtinr

"""
s1 = "Python"
s2 = "Luminar"
x=s1[0]+s2[0]
print(x)
m=s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
print(m)
l=s1[-1]+s2[-1]
print(y)
z=x+m+l
print(z)

