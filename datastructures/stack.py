# stack=[]
#
# # Use list append method to add element
# stack.append('a')
# stack.append('b')
# print("Stack:",stack)
# # Use peek to look at the top of the stack
# top=stack[-1]
# print("top of the stack:",top)


stack=[]
def push_element():
    element=input("enter the element:")
    stack.append(element)
    print(element,"is added to the stack")


def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(e,"is removed from the stack")

def top_element():
    top=stack[-1]
    print("top of the stack is",top)

def dsplay_stack():
    print(stack)

while True:
    choice=input("enter the choice:1.push 2.pop 3.top 4.display 5.quit\n")
    if choice=='1':
        push_element()
    elif choice=='2':
        pop_element()
    elif choice=='3':
        top_element()
    elif choice=='4':
        dsplay_stack()
    elif choice=='5':
        break
    else:
        print("invalid operation")