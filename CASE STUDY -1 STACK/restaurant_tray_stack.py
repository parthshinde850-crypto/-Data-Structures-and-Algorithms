class TrayStack:
    def __init__(self):
        self.stack = []
        self.limit = 30

    def add_tray(self, tray_no, clean, damaged):
        if len(self.stack) == self.limit:
            print("Tray stack is full.")
            return

        if not clean:
            print("Only clean trays can be added.")
            return

        if damaged:
            print("Damaged tray rejected.")
            return

        for tray in self.stack:
            if tray == tray_no:
                print("Tray number already exists.")
                return

        self.stack.append(tray_no)
        print(f"Tray {tray_no} added.")

    def remove_tray(self):
        if not self.stack:
            print("No trays available.")
            return

        tray = self.stack.pop()
        print(f"Removed Tray : {tray}")

    def top_tray(self):
        if not self.stack:
            print("No trays available.")
            return

        print("Top Tray :", self.stack[-1])


tray = TrayStack()

while True:
    print("\n1. Add Tray")
    print("2. Remove Tray")
    print("3. Top Tray")
    print("4. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        number = input("Tray Number : ")
        clean = input("Is tray clean? (yes/no) : ").lower() == "yes"
        damaged = input("Is tray damaged? (yes/no) : ").lower() == "yes"
        tray.add_tray(number, clean, damaged)

    elif choice == "2":
        tray.remove_tray()

    elif choice == "3":
        tray.top_tray()

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")