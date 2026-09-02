class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 20

    def push(self, plate_id, plate_stack):
        if len(self.stack) == 20:
            print("Stack is full")
            return 
        if plate_type != "steel" and plate_type != "ceramic":
            print("only steel and ceramic plates are allowed!")
            return
        for plate in self.stack:
            if plate[0] == plate_id:
                print("duplicate not allowed")
                return
        self.stack.append((plate_id, plate_stack))

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
    print("\n 1.push plate")
    print("2.pop plate")
    print("3.peek plate")
    print("4.display stack")
    print("5.exit")

    choice = int(input("Enter you choice:"))

    if choice == 1 :
        plate_id = int(input("Enter plate id:"))
        plate_type = input("Enter plate type:")
        s.push(plate_id, plate_type)

    elif choice == 2 :
        print("removed plate", s.pop())

    elif choice == 3:
        print("topmost plate", s.peek())

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")

