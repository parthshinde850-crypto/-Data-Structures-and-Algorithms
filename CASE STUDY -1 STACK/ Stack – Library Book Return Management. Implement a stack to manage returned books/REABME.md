class Stack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)
        print("Book returned:", book)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            book = self.stack.pop()
            print("Book removed:", book)

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Returned books:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


s = Stack()

s.push("Python")
s.push("DSA")
s.push("DBMS")

s.display()

s.pop()

s.display()
