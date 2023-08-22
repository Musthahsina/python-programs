"""find even numbers using lambda"""
numbers=[3,6,4,5,11,44,22,13,9,10,6,2]
even=list(filter(lambda  x:x%2==0,numbers))
print(even)


# """ Maximum of 3number using Lambda"""
# Max = lambda a, b: a if a>b else b
#
# print(Max(36, 82))