class BillingQueue:
    def __init__(self):
        self.queue = []
        self.limit = 40

    def add_customer(self, customer_id, cart):
        if len(self.queue) == self.limit:
            print("Queue is full.")
            return

        if not cart:
            print("Customer must have a shopping cart.")
            return

        if customer_id in self.queue:
            print("Customer ID already exists.")
            return

        self.queue.append(customer_id)
        print("Customer added.")

    def bill_customer(self):
        if not self.queue:
            print("Queue is empty.")
            return

        customer = self.queue.pop(0)
        print(f"Billing completed for {customer}")

    def next_customer(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("Next Customer :", self.queue[0])

    def display_queue(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("Billing Queue")
        for customer in self.queue:
            print(customer)


billing = BillingQueue()

while True:
    print("\n1. Add Customer")
    print("2. Bill Customer")
    print("3. View Next Customer")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        cid = input("Customer ID : ")
        cart = input("Has Shopping Cart? (yes/no) : ").lower() == "yes"
        billing.add_customer(cid, cart)

    elif choice == "2":
        billing.bill_customer()

    elif choice == "3":
        billing.next_customer()

    elif choice == "4":
        billing.display_queue()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")