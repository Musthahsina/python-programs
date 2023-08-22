# #check whether a number is prime or not
#
# num = 15
# flag = 0
#
# for i in range(2,num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 1:
#     print(num,"is not prime")
# else:
#     print(num,"is prime")
#
# #pgm to find those nos are divisible by 7 and multiple of 5
#
#
# n = int(input("enter the number:"))
# if n % 7 == 0 and n % 5 == 0:
#     print("number is divisible by 7 and not multiple of 5")
# else:
#     print("not divisible by 7 and multiple of 5")
#
# #vote or not
# #
# age = int(input("enter the age:"))
# if age >= 18:
#     print("the person is eligible to vote")
# else:
#     print("the person is  not eligible to vote")
#
#
# """
#
# """
# yos = int(input("enter year of service: "))
# salary = int(input("enter current salary: "))
# if yos >= 5:
#     salary = salary+salary*0.05
#     print("Rs:",salary,"is the incremented salary")
# else:
#     print("not eligible for salary increment")
#
#
# """
#
# """
#
# light=input("enter the light:")
# if light == "green":
#     print("car is allowed to go")
# elif light == "yellow":
#     print("car has to wait")
# elif light == "red":
#     print("car cannot go")
# else:
#     print("Invalid light")
# """
# A school has following rules for grading system:
#     a. Below 25 - F
#     b. 25 to 45 - E
#     c. 45 to 50 - D
#     d. 50 to 60 - C
#     e. 60 to 80 - B
#     f. Above 80 - A
#     Ask user to enter marks and print the corresponding grade.
# """
#
# mark = int(input("enter the mark:"))
#
# if mark <= 25:
#     print("Grade is: F")
# elif mark>=25 and mark < 45:
#     print("Grade is: E")
# elif mark >=45 and mark<=50:
#     print("Grade is: D")
# elif mark>= 50 and mark<=60:
#     print("Grade is: C")
# elif mark>=60 and mark<=80:
#     print("Grade is B")
# else:
#     print("Grade is:A")
#
#
# """
# . Take three int values from user and print greatest among them
# """
#
# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# c=int(input("enter 3rd no:"))
#
# if a>b and a>c:
#     print(a,"is greatest")
# elif  b>c:
#     print(b,"is greatest ")
# else:
#     print(c,"is greatest")


# even odd

# n=int(input("enter the number:"))
# if n%2==0:
#    print("even")
# else:
#     print("odd")

# palindrome

"""
logic:
str = input("string")
print(str[::-1])

"""
# str = input("string:")
# print(str[::-1])


# str = input("enter the string:\n")
#
# if str == str[::-1]:
#     print("String is palindrome")
# else:
#     print("Not palindrome")


# smallest

# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# c=int(input("enter 3rd no:"))
#
# if a<b and a<c:
#     print(a,"is smallest")
# elif  b<c:
#     print(b,"is smallest ")
# else:
#     print(c,"is smallest")
#

# palindrome number

# number = int(input("ente the no:"))
# rev = 0
# temp = number
# while number>0:
#     rem = number%10
#     #print(rem)
#     rev = (rev*10) + rem
#     #print(rev)
#     number = number//10
#
# if temp==rev:
#     print("palindrome")
# else:
#     print("not palindrome")


# fibonacci

# num = 10
# n1,n2 = 0,1
# for i in range(num):
#     print(n1,end='')
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     #print(n3,end='')
#

# amstrong
#
# number = int(input("enter the number:"))
# sum = 0
# temp = number
# while temp>0:
#     n = temp % 10 #153%10 = 3,15%10=5
#     sum = sum + n*n*n #0+3*3*3 - 27,27+%*5*5
#     temp = temp // 10 #153//10 = 15
# if number==sum:
#     print("amstrong")
# else:
#     print("not amstrong")

# wap to print sum of even nos and odd nos

# numbers= [3,6,7,5,11,8]
# esum=0
# osum=0
# for i in numbers:
#     if i%2==0:
#         esum=esum+i
#     else:
#         osum=osum+i
#
# print("Sum of even:",esum,"\nSum of odd:",osum)



"""
Write code of geartest common divisor
"""
# number1 = int(input("enter the number1: "))
# number2 = int(input("enter the number2: "))
# gcd=1
# for i in range(1,min(number1,number2)+1):
#     if (number1 % i == 0) and (number2 % i == 0):
#         gcd = i
# print("gcd is",gcd)

"""
Anagram or not
"""
# s1 = input("enter 1st string:")
# s2 = input("enter 2nd string:")
# s1 = list(s1)
# s2 = list(s2)
# s1.sort()
# s2.sort()
#
# if s1 == s2:
#     #print(s1==s2)
#     print("strings are anagram")
# else:
#     print("strings are not anagram ")

# swap two numbers

# n1=int(input("enter number1:"))
# n2=int(input("enter number2:"))
# temp=n1
# n1=n2
# n2=temp
# print(n1,"after swapping:",n2)
# print(n2,"after swapping:",n1)

#factorial

# a = int(input("enter a number"))
# f = 1
# for i in range(1,a+1):
#     f=f*i
#     print(f)
#
#
# a=input("enter the string1")
# b=input("enter the string 2")
# a=sorted(a.lower())
# print(a)
# b=sorted(b.lower())
# if (a==b):
#
#     print("anagram")
# else:
#     print("not anagram")

"""
leap yr or not
logic:
divisible by 400
divisible by 4 but not by 100
"""
# year = int(input("enter the year"))
# if year % 400 == 0 and year or year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# else:
#     print("Not Leap year")

"""
wap to check vowels or consonent
"""
# s=input("enter the letter:")
# v = ['a','e','i','o','u','A','E','I','O','U']
# for i in range(v):
# if s in v:
#     s.append(v)
#     print("vowels")
# else:
#     print("not vowels")
"""
wap that prints all nos 
"""
# for i in range(6):
#    if i==3:
#       continue
#    print(i)
# """
#mult.tbl of a given number

# n = int(input("enter the number:"))
# for i in range(1,11):
#    print(i,'x',n,'=',n*i)

#wap tomprint prime nos in a range
#
# prime=[]
# for i in range(1,50):
#    flag=0
#    if i<2:
#       continue
#    if i==2:
#       prime.append(2)
#       continue
#    for x in range(2,i):
#       if i % x == 0:
#          flag=1
#          break
#    if flag==0:
#       prime.append(i)
# print(prime)
#

# string = input("Please enter String : ")
# char = input("Please enter a Character : ")
# count = 0
# for i in range(len(string)):
#     if(string[i] == char):
#         count = count + 1
# print("Total Number of occurence of ", char, "is :" , count)
#
# num = int(input("Please enter the Maximum Number : "))
# dict = {}
#
# for i in range(1, num + 1):
#     dict[i] = i * i
#
# print("\nDictionary = ", dict)
#
# '''using set default'''
#
# num = int(input("Please enter the Maximum Number : "))
# dict = {}
#
# for i in range(1, num + 1):
#  dict.setdefault(i,i*i)
#
# print("\nDictionary = ", dict)
#
'''qtn4'''
# num = input("Input some comma seprated numbers : ").split(',')
# print(num)
# print(tuple(num))

'''Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

#
# import math
# c=50
# h=30
# value = []
# items=[x for x in input("enter the numbers:").split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print(','.join(value))
#
# import math
# c=50
# h=30
# sqr=[]
# num=list(map(int,(input("enter the number:").split())))
# for i in num:
#     Q=
'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

# val=[i for i in input("enter the words").split(',')]
# val.sort()
# print((',').join(val))

#method2
# words = input("Input words: ")
#
# list = words.split(",")
# list.sort()
#  print((', ').join(list))
#
# string1 = "calvin klein design dress calvin klein"
# words = string1.split()
# print (" ".join(sorted(set(words), key=words.index)))

'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''

# seq=input("enter the sequence:")
# word=[i for i in seq.split(' ')]
# print(' '.join(sorted(list(set(word)))))

'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''

# seq_val=[]
# values=[i for i in input("enter the values:").split(',')]
# print(values)
# for x in values:
#     int_x = int(x, 2)
#     print(int_x)
#     if not int_x % 5:
#         seq_val.append(x)
#         print(seq_val)
#
# print(','.join(seq_val))

'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

snt=input("enter the sentence:")
dict={"UPPER CASE":0, "LOWER CASE":0}
for char in snt:
    if char.isupper():
        dict["UPPER CASE"]+=1
    elif char.islower():
        dict["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", dict["UPPER CASE"])
print("LOWER CASE", dict["LOWER CASE"])

'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

lines = []
while True:
    sl = input("Enter lines:")
    if sl:
        lines.append(sl.upper())
    else:
        break;

for sl in lines:
     print(sl)

'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
snt =input("enter the sentence:")
dic={"DIGITS":0, "LETTERS":0}
for char in snt:
    if char.isdigit():
        dic["DIGITS"]+=1
    elif char.isalpha():
        dic["LETTERS"]+=1
    else:
        pass
print("LETTERS", dic["LETTERS"])
print("DIGITS", dic["DIGITS"])
