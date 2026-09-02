# stack

class Stack:
    def __init__(self):
        self.stack = []

   


    def push(self,x):
        if x == -1:
            return None
        else:
            return self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is underflow")
        else:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack[-1]
        
    def display(self):
        print(self.stack)

s = Stack()

while True:
    x = int(input("Enter element to push into stack:"))

    if x == -1:
        break
    s.push(x)

s.display()

print("pop", s.pop())
print("peek", s.peek())

s.display()



        