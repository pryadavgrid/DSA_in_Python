class Node:
    
    def __init__(self, data, next_node=None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkList:

    def __init__(self, head=None):
        self.head = head

    def add_node_at_the_end(self,value):
        my_current_node = Node(value)

        if self.head != None:
            temp = self.head
            while temp.next_node != None:
                temp = temp.next_node
            
            my_current_node.prev_node = temp
            temp.next_node = my_current_node

        else:
            self.head = my_current_node
        
    def print_front_to_back_doublylinked(self):
        temp = self.head
        while temp.next_node != None:
            print(temp.data)
            temp = temp.next_node

        print(temp.data)

    def print_back_to_front_doublylinked(self):
        temp = self.head

        while temp.next_node != None:
            temp = temp.next_node


        while temp.prev_node != None:
            print(temp.data)
            temp = temp.prev_node

        print(temp.data)



    def add_node_at_beg(self, value):
        temp = self.head
        my_current_node = Node(value)
        self.head = my_current_node
        my_current_node.next_node = temp
        temp.prev_node = my_current_node

    def add_node_specific_pos(self):
        pos = int(input("enter the pos : "))
        val = int(input("Enter Val : "))
        current_node = Node(val)

        temp = self.head

        n=1
        while(n < pos-1):
            temp = temp.next_node
            n = n+1

        temp2 = temp.next_node

        temp.next_node.prev_node = current_node
        temp.next_node = current_node
        current_node.prev_node = temp
        current_node.next_node = temp2

        # current_node.next_node = temp.next_node
        # current_node.prev_node = temp
        # temp.next_node = current_node
        # temp.prev_node = temp



        

root_node = DoublyLinkList()
root_node.add_node_at_the_end(10)
root_node.add_node_at_the_end(20)
root_node.add_node_at_the_end(30)
root_node.add_node_at_the_end(40)

root_node.add_node_at_beg(90)
root_node.add_node_specific_pos()

root_node.print_back_to_front_doublylinked()
# root_node.print_front_to_back_doublylinked()