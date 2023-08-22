"""1.Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)."""

# numbers = [n for n in range(1500,2701) if n % 7 == 0 and n % 5 == 0]
# print("numbers:",numbers)

# numbers = list(filter(lambda n: n % 7 == 0 and n % 5 == 0, range(1500, 2701)))
# print("numbers:", numbers)


"""2.Write a Python program to convert temperatures to and from Celsius and Fahrenheit?"""


# def celsius_to_fahrenheit(celsius_temp):
#     fahrenheit_temp = (celsius_temp * 9/5) + 32
#     return fahrenheit_temp

# def fahrenheit_to_celsius(fahrenheit_temp):
#     celsius_temp = (fahrenheit_temp - 32) * 5/9
#     return celsius_temp

# celsius_temp = 10
# fahrenheit_temp = 50

# fahrenheit_result = celsius_to_fahrenheit(celsius_temp)
# print(f"Celsius {celsius_temp} is equivalent to Fahrenheit {fahrenheit_result}")

# celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
# print(f"Fahrenheit {fahrenheit_temp} is equivalent to Celsius {celsius_result}")

# #using lambda

# celsius_to_fahrenheit = lambda celsius_temp:(celsius_temp * 9/5) + 32
# fahrenheit_to_celsius = lambda fahrenheit_temp : (fahrenheit_temp - 32) * 5/9
# print(celsius_to_fahrenheit(10))
# print(fahrenheit_to_celsius(50))

# # add = lambda x,y:x+y
# # print(add(10,5))

# """3.Write a Python program to check the validity of passwords input by users.
# {length of password should be between 6 to 16,atleast one small letter,One capital letter,one digit,
# and one special character}"""

import re
def is_valid(password):
    if len(password)<6 and len(password)>16:
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"[0-9]",password):
        return False
    if not re.search(r"[^A-Za-z0-9]",password):
        return False
    return True

password = input("enter the password:")
if len(password) < 6 or len(password) > 16:
    print("Password length should be between 6 and 16 characters.")
elif is_valid(password):
    print("password is valid")
else:
    print("password is not valid")

# """4.Write a Python program to check if a triangle is equilateral, isosceles or scalene. and show its area and
# perimeter."""

# import math

# side1 = int(input("Enter the length of side 1: "))
# side2 = int(input("Enter the length of side 2: "))
# side3 = int(input("Enter the length of side 3: "))

# if side1 == side2 == side3:
#     triangle_type = "equilateral"
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     triangle_type = "isosceles"
# else:
#     triangle_type = "scalene"

# perimeter = side1 + side2 + side3
# s = perimeter / 2   #s=semiperimeter
# area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3)) # Heron's formula

# print("The triangle is:",triangle_type)
# print("Perimeter:",perimeter)
# print("Area:",area)


# """5.Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they ty
# pe it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the ans
# wer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not an
# swer yes to the first question, display the answer “Enjoy your day”."""

# raining = input("Is it raining?(yes/no)").lower()
# if raining=="yes":
#     windy = input("Is it windy?(yes/no)").lower()
#     if windy=="yes":
#         print("It is too windy for an umbrella")
#     else:
#      print("Take an umbrella")
# else:
#     print("Enjoy your day")

# """6.Display the following message:{1:square
# 2:Triangle
# entrer a number} . If the user enters 1, then it should ask them for the length of one
# of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and d
# isplay the area. If they type in anything else, it should give them a suitable error message"""

# print("1:Square\n2:Triangle")
# choice = int(input("Enter a number:"))
# if choice == 1:
#     length = float(input("enter the length of one side of the square:"))
#     area = length * 2
#     print("Area of the square is:",area)
# elif choice==2:
#     base = float(input("Enter the base of the triangle:"))
#     height = float(input("Enter the height of the triangle:"))
#     area = base*height / 2
#     print("Area of the triangle is:",area)
# else:
#     print("Incorrect choice")

# """7.Write a Program to print duplicates from a list of integers"""

# def find_duplicates(list):
#     duplicates=[]
#     for item in list:
#         if list.count(item) > 1 and item not in duplicates:
#             duplicates.append(item)
#     return duplicates

# list = [2, 1, 3, 4, 3, 5, 2, 6, 1]
# print(find_duplicates(list))

"""8.Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, displ
ay the message “You can learn to drive”, if they are 16, display the message“You can buy a lott
ery ticket”,if they are under 16, display the message “You can go for treat”."""

age = int(input("enter your age:"))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go for a treat")

"""9.Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the na
mes and after each name display “[name] has been invited”. If they enter a number which is 10 or higher,
display the message “Too many people”."""

people = int(input("How many people do you want to invite to the party?"))
if people < 10:
    for i in range(people):
        name = input("Enter the name of the invited person:")
        print(name,"has been invited")
else:
    print("Too many people")

"""10.Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, dis
play “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message"""

choice = input("Enter 1,2 or 3:")
if choice == "1":
    print("Thank You")
elif choice == "2":
    print("Well done")
elif choice == "3":
    print("Correct")
else:
    print("Error message")


pswrd = input("Enter the password: ")
small_letter = False
capital_letter = False
digit = False
spec_character = False

if len(pswrd) >= 6 and len(pswrd) <= 16:
    for i in pswrd:
        if i.isdigit():
            digit = True
        if i.islower():
            small_letter = True
        if i.isupper():
            capital_letter = True
        if not i.isalnum():
            spec_character = True

    if digit and small_letter and capital_letter and spec_character:
        print("Password is valid")
    else:
        print("Password is invalid")
else:
    print("Password length should be between 6 and 16 characters.")
