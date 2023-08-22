def fibonacci(n1,n2):
    for i in range(1,11):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3
fibonacci(0,1)