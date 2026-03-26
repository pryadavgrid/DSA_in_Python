class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_element_at_rear(self, val):
        self.items.append(val)

    def insert_element_at_front(self, val):
        return self.items.insert(0, val)

    def delete_element_at_front(self):
        if self.is_empty() :
            print("Queue is empty")
            return
        
        return self.items.pop(0)
    

    def delete_element_at_rear(self):
        if self.is_empty() :
            print("Queue is empty")
            return
        
        return self.items.pop()


    
    def print_element(self):
        for item in self.items:
            print(item, end=" | ")



my_dequeue = Deque()

my_dequeue.insert_element_at_rear(20)
my_dequeue.insert_element_at_rear(30)
print("After insert two element at the rear")
my_dequeue.print_element()

my_dequeue.insert_element_at_front(10)
my_dequeue.insert_element_at_front(1)

print("\n\nAfter insert two element at the front")
my_dequeue.print_element()

my_dequeue.delete_element_at_front()

print("\n\nAfter delete element at the front")
my_dequeue.print_element()

my_dequeue.delete_element_at_rear()

print("\n\nAfter delete the element at the rear")

my_dequeue.print_element()