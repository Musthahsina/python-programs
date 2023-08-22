'''prime or not using function'''
num=int(input("enter the number:"))
if num > 1:
    # Check if factor exist
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Else if the input number is less than or equal to 1
else:
    print(num, "is not a prime number")
