class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None


    # Add node at beginning
    def add_node_at_the_beg(self, val):
        new_node = Node(val)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next_node = new_node
            new_node.prev_node = new_node
            return

        last = self.head.prev_node

        new_node.next_node = self.head
        new_node.prev_node = last

        last.next_node = new_node
        self.head.prev_node = new_node

        self.head = new_node


    # Add node at end
    def add_node_at_the_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            new_node.next_node = new_node
            new_node.prev_node = new_node
            return

        last = self.head.prev_node

        last.next_node = new_node
        new_node.prev_node = last
        new_node.next_node = self.head
        self.head.prev_node = new_node


    # Add node at specific position
    def add_node_specific_pos(self, pos, val):
        if pos == 1:
            self.add_node_at_the_beg(val)
            return

        new_node = Node(val)
        temp = self.head
        count = 1

        while count < pos - 1:
            temp = temp.next_node
            if temp == self.head:
                print("Position out of range")
                return
            count += 1

        next_node = temp.next_node

        temp.next_node = new_node
        new_node.prev_node = temp
        new_node.next_node = next_node
        next_node.prev_node = new_node


    # Delete from beginning
    def delete_beg_node(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next_node == self.head:
            self.head = None
            return

        last = self.head.prev_node

        self.head = self.head.next_node
        self.head.prev_node = last
        last.next_node = self.head


    # Delete from end
    def delete_end_node(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next_node == self.head:
            self.head = None
            return

        last = self.head.prev_node
        second_last = last.prev_node

        second_last.next_node = self.head
        self.head.prev_node = second_last


    # Delete from specific position
    def delete_node_from_specific_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.delete_beg_node()
            return

        temp = self.head
        count = 1

        while count < pos:
            temp = temp.next_node
            if temp == self.head:
                print("Position out of range")
                return
            count += 1

        prev_node = temp.prev_node
        next_node = temp.next_node

        prev_node.next_node = next_node
        next_node.prev_node = prev_node


    # Print from beginning
    def print_from_beg(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next_node
            if temp == self.head:
                break
        print()


    # Print from end
    def print_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head.prev_node

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev_node
            if temp == self.head.prev_node:
                break
        print()


# Testing
my_root_node = DoublyCircularLinkedList()

my_root_node.add_node_at_the_beg(20)
my_root_node.add_node_at_the_end(30)
my_root_node.add_node_at_the_beg(10)
my_root_node.add_node_specific_pos(2, 15)

print("Forward:")
my_root_node.print_from_beg()

my_root_node.delete_node_from_specific_pos(2)

print("After Deletion:")
my_root_node.print_from_beg()

print("Reverse:")
my_root_node.print_from_end()