'''calculator'''

def summ():
    sum=a+b
    print("sum",sum)
    return sum

def sub():
    sub=a-b
    print("sub",sub)
    return sub

def mult():
    mult=a*b
    print("mult",mult)
    return mult

def div():
    div=a/b
    print("div",div)
    return div

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=input("enter + to addition,- to subtraction,* to multiplication,/ to division\n")
if (c=="+"):
    summ()
elif(c=="-"):
    sub()
elif(c=="*"):
    mult()
elif(c=="/"):
    div()
else:
    print("invalid")
