# Node class represents one element of the doubly linked list
class Node:

    # Constructor to initialize node data and pointer references
    def __init__(self, data):
        # Store actual value of the node
        self.data = data

        # Pointer to next node in the list, Pointer to previous node in the list
        self.next_node = None
        self.prev_node = None

# Doubly Linked List class
class DoublyLinkList:

    def __init__(self):
        # Head pointer represents the first node of the list
        self.head = None


    # Insert a new node at the end of the linked list
    def add_node_at_the_end(self, val):
        # Create a new node with given value
        new_node = Node(val)

        # If list is empty, make new node the head
        if self.head == None:
            self.head = new_node
            return
        
        # Start traversal from head
        temp = self.head
        # Traverse until the last node
        while temp.next_node != None:
            temp = temp.next_node
        
        # Link last node with the new node
        temp.next_node = new_node
        new_node.prev_node = temp


    # Insert a node at the beginning of the list
    def add_node_at_the_beg(self,val):
        # Create new node
        new_node = Node(val)

        # If list is empty, new node becomes head
        if self.head == None:
            self.head = new_node
            return

        # Store current head node
        temp = self.head

        # New node points to current head, Update previous pointer of old head
        new_node.next_node = temp
        temp.prev_node = new_node
        self.head = new_node



    # Insert node at a specific position
    def add_node_specific_pos(self, pos, val):
        # Create new node
        new_node = Node(val)

        # Start traversal from head
        temp = self.head

        # If list is empty
        if temp == None:
            print("No Node Present")
            return
        
        # If position is 1, insert at beginning
        if pos == 1:
            self.add_node_at_the_beg(val)
            return

        # Counter to track current position
        counter = 1

        # Traverse until node before the target position
        while counter < pos - 1 and temp != None:
            counter = counter + 1
            temp = temp.next_node

        # If position exceeds list length
        if temp == None:
            print("Length Out Of Range")
            return
        
        # Store next node reference
        temp2 = temp.next_node

        temp.next_node = new_node
        new_node.prev_node = temp
        new_node.next_node = temp2

        # Update previous pointer of next node if it exists
        if temp2 != None:
            temp2.prev_node = new_node


    # Delete the first node of the list
    def delete_beg_node(self):
        # Store head node
        temp = self.head

        # If list is empty
        if temp == None:
            print("No Node Present")
            return
        
        # Store next node
        temp2 = temp.next_node

        if temp2 != None:
            temp2.prev_node = None

        self.head = temp2


    # Delete the last node of the list
    def delete_end_node(self):
        # Start from head
        temp = self.head

        # Check if list is empty
        if temp == None:
            print("Node Is Not Present")
            return

        # If only one node exists
        if temp.next_node == None:
            self.head = None
            return
        
        # Traverse to the last node
        while temp.next_node != None:
            temp = temp.next_node

        temp2 = temp.prev_node
        temp2.next_node = None

    # Delete node from a specific position
    def delete_node_from_specific_pos(self,pos):
        # Start traversal from head
        temp = self.head

        # If list is empty
        if temp == None:
            print("Node Is Not Present")
            return
        
        # If deleting first node
        if pos == 1:
            self.delete_beg_node()
            return
        
        # Position counter
        counter = 1
        
        # Traverse until desired position
        while pos > counter and temp != None:
            temp = temp.next_node
            counter = counter + 1

        # If position exceeds list length
        if temp == None:
            print("Position Out Of Range")
            return
        
        temp2 = temp.prev_node
        temp3 = temp.next_node

        temp2.next_node = temp3

        if temp3 != None:
            temp3.prev_node = temp2


    # Print nodes from beginning to end
    def print_node_from_beg(self):
        # Start from head
        temp = self.head

        # If list is empty
        if temp == None:
            print("No Node")
            return
        
        # Traverse and print node data
        while temp != None:
            print(temp.data)
            temp = temp.next_node


    # Print nodes from end to beginning
    def print_node_from_end(self):
        # Start from head
        temp = self.head

        # If list is empty
        if temp == None:
            print("No Node")
            return
        
        # Move to last node
        while temp.next_node != None:
            temp = temp.next_node

        # Traverse backward using prev_node pointer
        while temp != None:
            print(temp.data)
            temp = temp.prev_node


# Create a doubly linked list object
my_root_node = DoublyLinkList()

# Insert node at beginning
my_root_node.add_node_at_the_beg(20)

# Insert node at end
my_root_node.add_node_at_the_end(30)

# Insert node at position 3
my_root_node.add_node_specific_pos(3,10)

# Print list from beginning
print("Forword Printing")
my_root_node.print_node_from_beg()

# Delete node at position 1
my_root_node.delete_node_from_specific_pos(1)

# Print list in reverse order
print("\nReverse Printing\n")
my_root_node.print_node_from_end()