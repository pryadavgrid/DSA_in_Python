class Stack:

    # create a empty list
    def __init__(self):
        self.my_stack = []

    #  create a function which is return lenghth of stack
    def lenght_of_stack(self):
        return len(self.my_stack)
    
    # i let index 0 as a top index

    def push_element(self, val):
        self.my_stack.insert(0, val)

    def peek(self):
        if self.lenght_of_stack() == 0:
            raise Exception("Stack is empty")
        else:
            return self.my_stack[0]
        
    def pop_element(self):
        if self.lenght_of_stack() == 0:
            raise Exception("Stack is empty")
        else:
            return self.my_stack.pop(0)
        

stack = Stack()

stack.push_element(10)
stack.push_element(20)
stack.push_element(30)

print(stack.pop_element())
print(stack.pop_element())
print(stack.pop_element())

print(stack.peek())