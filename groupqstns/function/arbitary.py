# program to find sum of multiple numbers using arbitary arguments

def sum(*nums):
    result = 0

    for n in nums:
        result = result + n

    print("Sum = ", result)


sum(1, 2)
sum(4, 5, 7)