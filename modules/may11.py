# from may11 import sum
# print(sym(4,6))

'''builtin modules'''
import datetime

'''math module'''

import math
print(math.sqrt(5))
print(math.pi)
r=5
print(math.pi * r * r)

'''os module'''

import os
# os.mkdir(r'C:\Users\USER\PycharmProjects\pythonProject1\test')
# os.rmdir(r'C:\Users\USER\PycharmProjects\pythonProject1\test')

# to get current directory
print(os.getcwd())
# os.chdir('D:/')  '''change directory to d drive'''

'''random module'''

import random
# print(random.randrange(10))
# print(random.randint(1,100))
# a=[1,2,3,4,5]
# random.shuffle(a)
# print(a)
# string='computer'
# print(random.choice(string))
# print(random.random())
# print(random.randbytes(10))

from datetime import date
today=date.today()
print("today's date is:",today)

now=datetime.datetime.now()
print(now)

