# import json
# x='{"name":"reethu","age":28,"course":"python","guide":"priya"}'
# y=json.loads(x)
# print(y["age"],y["course"])
#
# ''''''
# import random
# s="mustahhsina"
# print(random.choice(s))
#
# import random
# print(random.randint(0,10)*5)

import turtle
x = turtle.Turtle()
# x.speed(1)
for i in range(2):
    x.fillcolor('green')
    x.begin_fill()
    x.forward(100)
    x.left(60)
    x.forward(50)
    x.left(120)
    x.end_fill()
turtle.done()

# list=[]
# for i in range(1000,3001):
#     x=str(i)
#     if (int(x[0])%2==0) and (int(x[1])%2==0) and (int(x[2])%2==0) and (int(x[3])%2==0):
#         list.append(x)
# print(','.join(list))
#
# lines = []
# while True:
#     sl = input()
#     if sl:
#         lines.append(sl.upper())
#     else:
#         break;
#
# for sl in lines:
#   print(sl)


