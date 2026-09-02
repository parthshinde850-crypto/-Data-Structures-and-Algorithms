class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# Creating binary tree
def create():
    x = int(input("Enter nodes to create binary tree:"))
    if x == -1:
        return None
    root = Node(x)

    print(f"Enter left child {x}")
    root.left = create()

    print(f"Enter right child {x}")
    root.right = create()

    return root

# stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        if data == -1:
            return None
        else:
            return self.stack.append(data)

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

# Non recursive preorder
def preorder(root):
    s = Stack()

    while root is not None or len(s.stack) != 0:
        while root is not None:
            print(root.data, end= " ")
            s.push(root)
            root = root.left
        
        root = s.pop()
        root = root.right

# Non recursive Inorder
def inorder(root):
    s = Stack()

    while root is not None or len(s.stack) != 0:
        while root is not None:
            s.push(root)
            root = root.left
        
        root = s.pop()
        print(root.data, end = " ")
        root = root.right

# Non recursive Postorder
def postorder(root):
    if root is None:
        return

    s1 = Stack()
    s2 = Stack()

    s1.push(root)
    
    while len(s1.stack) != 0:
        temp = s1.pop()
        s2.push(temp)

        if temp.left is not None:
            s1.push(temp.left)

        if temp.right is not None:
            s1.push(temp.right)

    while len(s2.stack) != 0:
        temp = s2.pop()
        print(temp.data, end =" ")
        


# Main
root = create()

print("\n Preorder Traversal")
preorder(root)


print("\n Inorder Traversal")
inorder(root)

print("\n Postorder Traversal")
postorder(root)



        
        

        
