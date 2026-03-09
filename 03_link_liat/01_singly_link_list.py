class Node:
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class SinglyLinkList:

    def __init__(self, head=None):
        self.head = head

    def add_node_at_the_end(self,value):
        my_current_node = Node(value)

        if self.head != None:
            temp = self.head
            while temp.next_node != None:
                temp = temp.next_node
            
            temp.next_node = my_current_node
        else:
            self.head = my_current_node
        
    def print_singly_link_list(self):
        temp = self.head

        while temp != None:
            print(temp.data)
            temp = temp.next_node

    def add_node_at_beg(self, value):
        temp = self.head
        my_current_node = Node(value)
        self.head = my_current_node
        self.head.next_node = temp

    def add_node_specific_pos(self, pos, value):

        current_node = Node(value)

        temp = self.head
        
        if pos == 1:
            current_node.next_node = temp
            self.head = current_node
        else:
            n=1
            while(n < pos-1 and temp != None):
                temp = temp.next_node
                n = n + 1
            if temp == None:
                print("Out Of Index")
            else:
                current_node.next_node = temp.next_node
                temp.next_node = current_node


    def delete_node(self, val):
        if self.head == None:
            print("List Is Empty")
        else:
            temp = self.head
            temp2 = temp.next_node

            if val == self.head.data:
                self.head = temp2
            else:
                while(temp2 != None):
                    if(temp2.data == val):
                        temp.next_node = temp2.next_node
                        break
                    else:
                        temp2 = temp2.next_node
                        temp = temp.next_node
                if(temp2 == None):
                    print("Value Is Not Present")
            


root_node = SinglyLinkList()
root_node.add_node_at_the_end(10)
root_node.add_node_at_the_end(20)
root_node.add_node_at_the_end(30)
root_node.add_node_at_the_end(40)
root_node.add_node_at_the_end(50)
root_node.add_node_at_the_end(60)
root_node.add_node_at_beg(70)
root_node.add_node_specific_pos(8, 70)

root_node.print_singly_link_list()
# print()
root_node.delete_node(60)
root_node.print_singly_link_list()