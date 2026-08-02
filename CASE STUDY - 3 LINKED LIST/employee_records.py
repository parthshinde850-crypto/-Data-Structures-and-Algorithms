class Node:
    def __init__(self, emp):
        self.emp = emp
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, emp):
        node = Node(emp)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.emp, end=" -> " if temp.next else "")
            temp = temp.next
        print()


employees = LinkedList()

employees.insert("E201")
employees.insert("E202")
employees.insert("E203")
employees.insert("E204")
employees.insert("E205")

print("Employee List")
employees.display()

employees.delete_head()

print("\nUpdated List")
employees.display()

print("\nHead now points to:", employees.head.emp)