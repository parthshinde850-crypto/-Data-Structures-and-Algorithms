class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Creating binary tree
def create():
    x = int(input("Enter nodes to create binary tree:"))
    if  x == -1:
        return None
    root = Node(x)

    print(f"enter left node {x}")
    root.left = create()
    print(f"Enter right node{x}")
    root.right = create()

    return root

def preorder(temp):    #temp is a variable name given we can use node or root or x
    if temp is not None:
        print(temp.data , end=" ")
        preorder(temp.left)
        preorder(temp.right)

def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)

def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")

root = create()

print("\n Preorder Traversal")
preorder(root)

print("\n Inorder Traversal")
inorder(root)

print("\n Postorder Traversal")
postorder(root)



