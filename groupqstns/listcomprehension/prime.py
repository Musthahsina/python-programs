List=[2,3,4,5,6,7,8,9,10,11,12]
prime=[i for i in List if 0 not in [i%j for j in range(2,i//2)]]
print("prime numbers in the list:",prime)