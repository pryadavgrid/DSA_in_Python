class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_element(self, val):
        self.items.append(val)

    def delete_element(self):
        if self.is_empty() :
            print("Queue is empty")
            return
        
        return self.items.pop(0)
    
    def print_element(self):
        for item in self.items:
            print(item, end=" | ")
    

my_queue = Queue()

my_queue.insert_element(10)
my_queue.insert_element(20)
my_queue.insert_element(30)


print(my_queue.delete_element())
my_queue.print_element()