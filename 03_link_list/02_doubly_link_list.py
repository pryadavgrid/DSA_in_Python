class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkList:

    def __init__(self):
        self.head = None


    def add_node_at_the_end(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next_node != None:
            temp = temp.next_node
        
        temp.next_node = new_node
        new_node.prev_node = temp


    def add_node_at_the_beg(self,val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            return

        temp = self.head

        new_node.next_node = temp
        temp.prev_node = new_node
        self.head = new_node


    def add_node_specific_pos(self, pos, val):
        new_node = Node(val)

        temp = self.head

        if temp == None:
            print("No Node Present")
            return
        
        if pos == 1:
            self.add_node_at_the_beg(val)
            return

        counter = 1

        while counter < pos - 1 and temp != None:
            counter = counter + 1
            temp = temp.next_node

        if temp == None:
            print("Length Out Of Range")
            return
        
        temp2 = temp.next_node

        temp.next_node = new_node
        new_node.prev_node = temp
        new_node.next_node = temp2

        if temp2 != None:
            temp2.prev_node = new_node


    def delete_beg_node(self):
        temp = self.head

        if temp == None:
            print("No Node Present")
            return
        
        temp2 = temp.next_node

        if temp2 != None:
            temp2.prev_node = None

        self.head = temp2


    def delete_end_node(self):
        temp = self.head

        if temp == None:
            print("Node Is Not Present")
            return

        # only one node
        if temp.next_node == None:
            self.head = None
            return
        
        while temp.next_node != None:
            temp = temp.next_node

        temp2 = temp.prev_node
        temp2.next_node = None


    def delete_node_from_specific_pos(self,pos):
        temp = self.head

        if temp == None:
            print("Node Is Not Present")
            return
        
        if pos == 1:
            self.delete_beg_node()
            return
        
        counter = 1
        
        while pos > counter and temp != None:
            temp = temp.next_node
            counter = counter + 1

        if temp == None:
            print("Position Out Of Range")
            return
        
        temp2 = temp.prev_node
        temp3 = temp.next_node

        temp2.next_node = temp3

        if temp3 != None:
            temp3.prev_node = temp2


    def print_node_from_beg(self):
        temp = self.head

        if temp == None:
            print("No Node")
            return
        
        while temp != None:
            print(temp.data)
            temp = temp.next_node


    def print_node_from_end(self):
        temp = self.head

        if temp == None:
            print("No Node")
            return
        
        while temp.next_node != None:
            temp = temp.next_node

        while temp != None:
            print(temp.data)
            temp = temp.prev_node



my_root_node = DoublyLinkList()

my_root_node.add_node_at_the_beg(20)
my_root_node.add_node_at_the_end(30)
my_root_node.add_node_specific_pos(3,10)

print("Forward:")
my_root_node.print_node_from_beg()

my_root_node.delete_node_from_specific_pos(1)

print("\nReverse Printing\n")
my_root_node.print_node_from_end()