class circular_queue:

    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = -1
        self.rear = -1


    def add_element(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1 :
            self.front = 0
            self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value


    def remove_element(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.rear == self.front:
            self.items[self.rear] = None
            self.rear = -1
            self.front = -1
        else:
            self.items[self.front] = None
            self.front = (self.front + 1) % self.size

    def dispaly_items(self):
        for i in self.items:
            print(i)


my_circular_queue = circular_queue(5)

my_circular_queue.add_element(10)
my_circular_queue.add_element(20)
my_circular_queue.add_element(30)
my_circular_queue.add_element(40)
my_circular_queue.add_element(50)

my_circular_queue.remove_element()
my_circular_queue.remove_element()
my_circular_queue.remove_element()
my_circular_queue.remove_element()
my_circular_queue.remove_element()

my_circular_queue.add_element(10)
my_circular_queue.add_element(20)
my_circular_queue.add_element(30)
my_circular_queue.add_element(40)
my_circular_queue.add_element(50)


my_circular_queue.remove_element()
my_circular_queue.add_element(60)
my_circular_queue.remove_element()
my_circular_queue.add_element(70)
my_circular_queue.remove_element()
my_circular_queue.add_element(80)
my_circular_queue.remove_element()
my_circular_queue.add_element(90)
my_circular_queue.remove_element()
my_circular_queue.add_element(100)
my_circular_queue.remove_element()





my_circular_queue.dispaly_items()