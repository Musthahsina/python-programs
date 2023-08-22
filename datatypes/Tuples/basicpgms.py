"""
1.to check whether an element exist in  a tuple
tuple1=("Apple",[10,20,30],(5,12,25),1,5,6,7)

2.to convert a tuple into a string
tuple2=("s","t","r","i","n","g")

3.count the number of occurance of item 50 from a tuple
tuple3=(20,50,70,50,60)


"""
tuple1 = ("Apple",[10,20,30],(5,12,25),1,5,6,7)
print("Apple" in tuple1)


tuple2 = ("s","t","r","i","n","g")
x="".join(tuple2)
print(x)

tuple3=(20,50,70,50,60)
a=tuple3.count(50)
print(a)

y=enumerate(tuple2)
v= (list(y))
print(v)
print(type(v))


tuples = ( 0,4,5,6,7,False,True)
print(all(tuples))
print(any(tuples))

