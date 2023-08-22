# squaredict={}
# for num in range(1,11):
#     squaredict[num]=num*num
# print(squaredict)
#
# '''dict-cmprhnsn'''
# #square
#
# squaredict={num:num*num for num in range(1,11)}
# print(squaredict)
#
# #even
#
# squaredict={num:2*num for num in range(1,11)}
# print(squaredict)
#
# old_price={'milk':1.02,'coffee':2.5,'bread':2.5}
# dollar_to_pound=0.76
# new_price={key:value*dollar_to_pound for (key,value) in old_price.items()}
# print(new_price)
#
# keys=['a','b','c','d','e']
# values=[1,2,3,4,5]
# print(dict(zip(keys,values)))
#
# dict={k:v for (k,v)in zip (keys,values)}
# print(dict)


# odd/even

# dict={k:'even' if k%2==0 else'odd' for k in range(1,11)}
# print(dict)
# #
# keys=['a','b','c','d','e','f']
# dict = {keys[i]:keys[i+1] for i in range(0,len(keys),2)}
# print(dict)
#
# lst=['a','b','c','d','e','f']
# dict={k:v for v,k in enumerate(lst)}
# print(dict)

# keys=['a','b','c','d','e','f']
# first_value=[keys[i] for i in range(0,len(keys),2)]
# second_value=[keys[j] for j in range(1,len(keys),2)]
# print(dict(zip(first_value,second_value)))


