# """ A function called itself """
#
# """ factorial of a number"""
# def fact(n):
#     if n==1:
#         print(n)
#         return 1
#     else:
#         x= n* fact(n-1)
#         print(x)
#         return x
# print("factorial:",fact(5))
# print("_____________________________________")
#
# """ sum of first 10 numbers"""
# def counter(c):
#     if c<=0:
#         print(c)
#         return c
#     else:
#         x=c+counter(c-1)
#         print(x)
#         return x
#         #return c+counter(c-1)
# print("Sum of first n numbers:",counter(10))
# print("_____________________________________")
#
# """ Another way"""
# def another(k):
#     if k>0:
#         result = k+ another(k-1)
#         print(result)
#         return result
#     else:
#         result=0
#         print(result)
#     return result
# print(another(5))
# print("_____________________________________")
#
# """ sum of digits"""
# def digit_sum(n):
#     if n==0:
#         return 0
#     else:
#         digit = n%10
#         sum = digit + digit_sum(int(n//10))
#         return sum
# result = digit_sum(34)
# print(result)
# print("_____________________________________")
#
# """ fibonacci"""
# def fib(n):
#      if n==0:
#          print(n)
#          return 0
#      elif n==1:
#          print(n)
#          return 1
#      else:
#          f= (fib(n-1)+fib(n-2))
#          print(f)
#          return f
#
# print(fib(5))

'''string palindrome'''

# s=input('enter the string:')
# def ispalindrome(s):
#     if len(s) <=1:
#         return True
#     else:
#         if s[0]==s[-1]:
#             return ispalindrome(s[1:-1])
#         else:
#             return False
# print(ispalindrome(s))
# x = s[1:-1]
# print(x)

'''sum of digits'''
# l=[]
# def sum_digits(b):
#     if(b==0):
#         return l
#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)
# n=int(input("Enter a number: "))
# sum_digits(n)
# print(sum(l))
# # print(0%10)

# n=200
# def sum_of_digit(n):
#     if n<10:
#         return n
#     else:
#         return n%10+sum_of_digit(n//10)
# print(sum_of_digit(n))
#
# '''product of digits'''
# n=234
# def pdt_of_digit(n):
#     if n<10:
#         return n
#     else:
#         return n%10*sum_of_digit(n//10)
# print(pdt_of_digit(n))
