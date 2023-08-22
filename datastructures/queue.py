queue=[]
def en_queue():
 element=input("enter the element:")
 queue.append(element)
 print(element,"is added to the queue")

def de_queue():
    if not queue:
        print("stack is empty")
    else:
        e=queue.pop(0)
        print(e,"is removed from queue:")

def show_queue():
    print(queue)

while True:
    choice=input("enter the choice:1.add 2.remove 3.show 4.quit\n")
    if choice=='1':
        en_queue()
    elif choice=='2':
        de_queue()
    elif choice=='3':
        show_queue()
    elif choice=='4':
        break
    else:
        print("invalid operation")