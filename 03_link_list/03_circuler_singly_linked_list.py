class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class circulerSinglyLinkedList:
    
    def __init__(self):
        self.head = None


    def add_node_at_the_end(self, value):
        new_node = Node(value)

        temp = self.head

        if temp == None:
            self.head  = new_node
            return
        
        while temp.next_node != None and temp.next_node != self.head:
            temp = temp.next_node

        temp.next_node = new_node
        new_node.next_node = self.head


    def add_node_at_beg(self, val):
        new_node = Node(val)

        temp = self.head
        
        if temp == None:
            self.head = new_node
            return
        
        new_node.next_node = temp
        self.head = new_node

        temp2 = temp

        while temp.next_node != None and temp.next_node != temp2:
            temp = temp.next_node

        temp.next_node = self.head


    def add_node_specific_pos(self, val, pos):
        new_node = Node(val)

        temp = self.head

        if temp == None:
            self.head = new_node
            return
        
        if pos == 1 :
            self.add_node_at_beg(val)
            return

        count = 1

        while pos - 1  > count and temp.next_node != self.head:
            temp = temp.next_node
            count = count + 1 

        if temp.next_node == self.head:
            print("Out Of Range")
            return

        temp2 = temp.next_node

        temp.next_node = new_node
        new_node.next_node = temp2


    def delete_from_beg(self):
        temp = self.head

        if temp == None:
            print("No Node Present")
            return
        
        temp2 = temp.next_node

        while temp.next_node != self.head:
            temp = temp.next_node

        temp.next_node = temp2
        self.head = temp2


    def delete_from_end(self):
        temp = self.head

        if temp == None:
            print("No Node Present")
            return
        

        while temp.next_node != self.head:
            temp2 = temp
            temp = temp.next_node

        temp2.next_node = self.head


    def delete_from_sepecific_pos(self, pos):
        temp = self.head

        if pos == 1:
            self.delete_from_beg()
            return

        if temp ==  None:
            print("No Node Present")
            return
        
        counter = 1

        while pos > counter and temp.next_node != self.head:
            counter = counter + 1
            temp2 = temp
            temp = temp.next_node

        temp2.next_node = temp.next_node
        



    def printsingly_link_list(self):
        temp = self.head

        if temp == None:
            print("Node Is Not Present")
            return
        
        while temp.next_node != self.head :
            print(temp.data)
            temp = temp.next_node

        print(temp.data)

    




root_node = circulerSinglyLinkedList()
root_node.add_node_at_the_end(10)
root_node.add_node_at_beg(5)
root_node.add_node_at_the_end(20)
root_node.add_node_at_beg(1)

# root_node.delete_from_beg()
# root_node.delete_from_end()
root_node.printsingly_link_list()

root_node.delete_from_sepecific_pos(1)

# root_node.add_node_specific_pos(90,1)
print()
root_node.printsingly_link_list()