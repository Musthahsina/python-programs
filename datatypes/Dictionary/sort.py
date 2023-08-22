dict={5:2,6:4,7:3,8:1,9:0}
val=list(dict.items())
print(val)

newval=[]
newvalf=[]
for i in val:
    irev=i[::-1]
    newval.append(irev)
print(newval)
#val.clear()
newval.sort()
print(newval)

for i in newval:
    irevf=i[::-1]
    newvalf.append(irevf)
print(newvalf)

dec=newvalf[::-1]
print(dec)


# listofdict=[{"V":"5001"},{}]