class Stack:

    # create a empty list
    def __init__(self):
        self.my_stack = []


    #  create a function which is return lenghth of stack
    def lenght_of_stack(self):
        return len(self.my_stack)
    

    # Here, index 0 is considered as the top.
    def push_element(self, val):
        self.my_stack.insert(0, val)


    # Returns the top element without removing it.
    def peek(self):
        if self.lenght_of_stack() == 0:
            raise Exception("Stack is empty")
        else:
            return self.my_stack[0]
        
    # Removes and returns the top element.
    def pop_element(self):
        if self.lenght_of_stack() == 0:
            raise Exception("Stack is empty")
        else:
            return self.my_stack.pop(0)
        


# Create Stack 
stack = Stack()

# Push Elements
stack.push_element(10)
stack.push_element(20)
stack.push_element(30)

# Pop Elements
print(stack.pop_element())
print(stack.pop_element())
print(stack.pop_element())


# Peek
# This will raise an exception because stack is empty.
print(stack.peek())