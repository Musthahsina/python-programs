List=[-1,2,-4,5,3,-9,8]
pos=[i for i in List if i>=0]
neg=[i for i in List if i not  in pos]
print(pos)
print(neg)

