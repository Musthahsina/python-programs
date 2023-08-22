# full pyramid of *
import string

# n = int(input("Enter the levels you want: "))
#
# for i in range(1, n + 1):  # rows
#     for j in range(n - i):  # spaces
#         print(' ', end='')
#     for k in range(i):
#         print('*', end=' ')
#     print()


# n=int(input("enter the levels you want:"))
#
# for i in range(1,n+1): #rows
#     for j in range(i): #spaces
#         print(' ',end=' ')
#     for k in range(n-i):
#         print(' * ',end=' ')
#     print()

# diamond
#
# n=int(input("enter the levels you want:"))
#
# for i in range(1,n+1): #rows
#     for j in range(n-i): #spaces
#         print('',end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()
#
# for i in range(1,n+1): #rows
#     for j in range(i): #spaces
#         print('',end=' ')
#     for k in range(n-i):
#         print('*',end=' ')
#     print()

# hollow diamond

# n = int(input("Enter the limit  :"))
# for i in range(n+1):# for loop for upper triangle   ( No: of rows )
#     for j in range(n-i+1):# for spacing
#         print(' ', end = ' ')
#     for k in range(1, 2*i):# pattern printing
#         if k==1  or k==2*i-1: # [k==1 for left]  [k==2*i-1  for right]
#             print('*',  end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# for i in range(n+1, 0, -1):
#     for j in range(1, n-i+2):
#         print(' ', end=' ')
#     for k in range(1, 2*i):
#         if k==1 or k==2*i-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#

# # 5)half pyramid 0f number

# n=int(input("enter the levels you want:"))
#
# for i in range(n+1):
#     print('', end = ' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()


# # 6) reverse from 1-10

# row=int(input("enter the levels you want:"))
#
# for i in range(row+1,0,-1):
#     print('', end = ' ')
#     for j in range(1,i):
#         i=i-1
#         print(i, end=' ')
#     print()

# row=int(input("enter the levels you want:"))
#
# for i in range(row+1,0,-1):
#     print('', end = ' ')
#     for j in range(i-1,0,-1):
#         print(j, end=' ')
#     print()

# hourglass

# n=int(input("enter the row:"))
#
# for i in range(n): #rows
#     for j in range(i): #spaces
#         print('',end=' ')
#     for k in range(n-i):
#         print('*',end=' ')
#     print()
#
# for i in range(1,n+1): #rows
#     for j in range(n-i): #spaces
#         print('',end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# hollow
#
# n=int(input("enter an odd number:"))
# for row in range(n):
#    for col in range (n):
#        if row+col==(n//2) or col-row==(n//2) or row-col==(n//2) or row+col==3*(n//2):
#            print(" * ",end='')
#        else:
#            print('  ',end='')
#    print()

# half pyramid of abcd...

# n=int(input("enter the levels you want:"))
# ascii=65
# for i in range(n):
#     print('', end = ' ')
#     for j in range(i+1):
#         print(chr(ascii), end=' ')
#         ascii += 1
#     print()

# #full
#
# rows = int(input("Please enter the number of rows : "))
# ascii = 65
# for i in range(1, rows + 1):
#     for j in range(rows - i ):
#         print('',end = ' ')
#     for k in range(i):
#         print(chr(ascii), end = ' ')
#         ascii += 1
#     print()


# inverted full pyramid
# n = int(input("enter the level:"))
# for i in range(n + 1):  # rows
#     for j in range(i):  # spacing
#         print(' ', end=' ')
#     for k in range(n - i):  # no of * print
#         print('  *', end=' ')
#     print()
#
# cross
# n = int(input("enter the limit:"))
# for rows in range(n):
#   for cols in range(n):
#     if((rows == cols) or (rows+cols)==n-1 ):
#       print(min(rows, n - rows - 1),end="")
#     else:
#       print(" ",end="")
#   print()

# alphabets

# A=65
# for i in range(97,123):
#     print(chr(i),end=" ")

# import string
#
# for i in string.ascii_uppercase:
#     print(i,end=" ")
# another way of half pyramid of alphabets

# n=int(input("enter level:"))
# k=1
# for i in  range(1,n+1):
#     for j in range(i):
#         print(chr(64+k),end=" ")
#         k+=1
#     print()
# n = int(input("Please enter the number of rows : "))
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end=' ')
#     print()


# num=int(input("enter level:"))
# for i in range(65,65+num):
#     for j in range(65,i+1):
#         print(chr(j),end=' ')
#     print()

# num=int(input("enter level:"))
# for i in range(65,65+num):
#     for j in range(65,i+1):
#         print(chr(i),end=' ')
#     print()

# num = int(input("Please enter the number of rows : "))
# # ascii = 65
# y=1
# for i in range(1, num + 1):
#     for j in range(num - i ):
#         print('',end = ' ')
#     for k in range(i):
#         print( chr(64+y) , end = ' ')
#         y += 1
#     print()

#
# n = int(input("enter the rows:"))
# k = 0
# for i in range(n, 0, -1):
#     k += 1
#     for j in range(1, i + 1):
#         print(k, end=' ')
#     print()

# Same character pattern
# char = 'B'
# charascii = ord(char)
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         character = chr(charascii)
#         print(char, end=' ')
#     print()

# n=int(input("enter the levels you want:"))
# for i in range(1,n+1):
#     for j in range(n):
#         print(i, end=' ')
#     print()

# n=int(input("enter the levels you want:"))
#
# for i in range(n): #rows
#     for j in range(i+1): #spaces
#         print('',end='')
#     for k in range(i):
#         print('*',end='')
#     print()
# for i in range(n,0,-1): #rows
#     for j in range(i-1): #spaces
#         print('',end='')
#     for k in range(i):
#         print('*',end='')
#     print()
#
# n=int(input("enter the number:"))
# rev=''
# while n>0:
#     rem=n%10
#     rev=rev+str(rem)
#     # print(str(rem))
#     n=n//10
# print("reverse is:",rev)

n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()