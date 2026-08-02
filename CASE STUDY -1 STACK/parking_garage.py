class ParkingGarage:
    def __init__(self):
        self.stack = []
        self.limit = 10

    def park_vehicle(self, number, vehicle_type):
        if len(self.stack) == self.limit:
            print("Parking is full.")
            return

        vehicle_type = vehicle_type.lower()

        if vehicle_type not in ["car", "bike"]:
            print("Only Car and Bike are allowed.")
            return

        for vehicle in self.stack:
            if vehicle["number"] == number:
                print("Vehicle number already exists.")
                return

        self.stack.append({
            "number": number,
            "type": vehicle_type
        })

        print("Vehicle parked successfully.")

    def remove_vehicle(self):
        if not self.stack:
            print("Parking is empty.")
            return

        vehicle = self.stack.pop()
        print(f"{vehicle['type'].title()} {vehicle['number']} left the parking.")

    def top_vehicle(self):
        if not self.stack:
            print("Parking is empty.")
            return

        vehicle = self.stack[-1]
        print("Last Parked Vehicle")
        print("Number :", vehicle["number"])
        print("Type   :", vehicle["type"].title())


garage = ParkingGarage()

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Last Parked Vehicle")
    print("4. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        number = input("Enter Vehicle Number : ")
        vehicle_type = input("Enter Vehicle Type (Car/Bike) : ")
        garage.park_vehicle(number, vehicle_type)

    elif choice == "2":
        garage.remove_vehicle()

    elif choice == "3":
        garage.top_vehicle()

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")