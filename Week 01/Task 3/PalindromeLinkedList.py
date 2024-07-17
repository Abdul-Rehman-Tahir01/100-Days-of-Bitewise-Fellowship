# Implemented OOP

class Node:
    def __init__(self, data=None):   # Constructor
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):    # Constructor
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)   # Linking the individual nodes of linked list by populating the next field of each node with the reference of next node.

    def print_list(self):
        current = self.head
        data_list = []
        while current:
            print(current.data, end = " -> " if current.next else "")
            data_list.append(current.data)
            current = current.next
        return data_list 

# Test Code
linked_list = LinkedList()
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node_data = input(f"Enter data for node {i+1}: ")
    linked_list.append(node_data)

print('\n')
data_list = linked_list.print_list()

# Checking if the list is palindrome
panlindrome = True

for i in range(num_nodes):
    if data_list[i] != data_list[num_nodes - 1 - i]:
        print("\n\nThe linked list is not a palindrome.")
        panlindrome = False
        break
    
if panlindrome:
    print("\n\nThe linked list is a palindrome.")
