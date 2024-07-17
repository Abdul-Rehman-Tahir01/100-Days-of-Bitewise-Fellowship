class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " -> " if current.next else "")
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Code starts here
linked_list = LinkedList()

num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node_data = input(f"Enter data for node {i+1}: ")
    linked_list.append(node_data)

print('\n')
linked_list.print_list()

# Reversing the linked list
linked_list.reverse_list()
print('\n')
linked_list.print_list()