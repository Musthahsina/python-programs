"""

Lists
--------

Ordered
Changeable
Allow Duplicates


"""

thislist = ["apple", "orange","mango", "grapes"]
print(thislist)

#indexing

print(thislist[2])
print(thislist[-1])
print(thislist[:-1])
print(thislist[1:])
print(thislist[0][-1])
print(thislist[3][-3])
print(thislist[0][:-1])
print(thislist[0][::-1])

#changing

x=thislist[1]='pineapple'
print(thislist)

str1="hi dears"

x=list(str1)
print(x)
x[1]="v"
print(x)
print("".join(x))
x=thislist[2].replace('mango',"#")
print(x)
thislist= ["apple", "orange","mango", "grapes",["python","django","react","java"]]
print(thislist[4][0])
print(thislist[4][0][0])
thislist[4][1]='Angular'
print(thislist)
thislist.append("vue.js")
print(thislist)
thislist[4].insert(1,"goleng")
print(thislist)
thislist.remove("apple")
print(thislist)
thislist.pop(1)
#thislist.clear()
#print(thislist)
#del thislist
#print(thislist)
y=thislist.count("orange")
print(y)
#thislist.reverse()
#print(thislist)
thislist=["apple", "orange","mango", "grapes",["python","django","react","java"]]
thislist[4].sort()
print(thislist)
x=["python","django","react","java"]
x.sort(reverse=True)
print(x)



