class LibraryQueue:
    def __init__(self):
        self.queue = []
        self.limit = 75

    def return_book(self, book_id, borrowed):
        if len(self.queue) == self.limit:
            print("Return queue is full.")
            return

        if not borrowed:
            print("Only borrowed books can be returned.")
            return

        if book_id in self.queue:
            print("Book ID already exists.")
            return

        self.queue.append(book_id)
        print("Book returned successfully.")

    def process_return(self):
        if not self.queue:
            print("No books to process.")
            return

        book = self.queue.pop(0)
        print(f"Processed Book : {book}")

    def next_book(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("Next Book :", self.queue[0])

    def display_queue(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("Books Waiting for Processing")
        for book in self.queue:
            print(book)


library = LibraryQueue()

while True:
    print("\n1. Return Book")
    print("2. Process Return")
    print("3. View Next Book")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        book = input("Book ID : ")
        borrowed = input("Was the book borrowed? (yes/no) : ").lower() == "yes"
        library.return_book(book, borrowed)

    elif choice == "2":
        library.process_return()

    elif choice == "3":
        library.next_book()

    elif choice == "4":
        library.display_queue()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")