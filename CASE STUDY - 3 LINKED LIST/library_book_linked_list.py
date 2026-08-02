class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.book, end=" -> " if temp.next else "")
            temp = temp.next
        print()


books = LinkedList()

books.insert("B101")
books.insert("B102")
books.insert("B103")
books.insert("B104")
books.insert("B105")

print("Final Linked List")
books.display()