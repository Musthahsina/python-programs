def simpleinterest(p, t, r):
    si = (p * t * r) / 100
    return si
p=int(input("enter the principal amount:"))
t=int(input("enter the time period:"))
r=float(input("enter the rate of interest:"))
print("simple interest is:", simpleinterest(p, t, r))

'''leap year'''
def leap_or_not(year):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
             print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
year = int(input("enter the year:"))
leap_or_not(year)

'''perfect number'''

def perfect_num(n):
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum=sum+i
    return sum

n=int(input("enetr the number:"))

if (n==perfect_num(n)):
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")

'''Last name fixed'''


def myfn(fname):  #default argument or parameter value
    print(fname + ' Alukkal')
myfn("Musthahsina")
myfn("Dilshad")

