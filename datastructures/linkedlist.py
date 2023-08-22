# Node class representing a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to traverse and print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Printing the linked list
print_linked_list(node1)
