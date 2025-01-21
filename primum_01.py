class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__cost = None
        self.__premium_amount = None

    # Getter and Setter methods
    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_type(self, vehicle_type):
        if vehicle_type not in ["Two Wheeler", "Four Wheeler"]:
            raise ValueError("Invalid vehicle type. Must be 'Two Wheeler' or 'Four Wheeler'.")
        self.__vehicle_type = vehicle_type

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_premium_amount(self):
        return self.__premium_amount

    # Public methods
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = 0.02 * self.__cost
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = 0.06 * self.__cost

    def display_vehicle_details(self):
        print(f"Vehicle ID: {self.__vehicle_id}")
        print(f"Vehicle Type: {self.__vehicle_type}")
        print(f"Vehicle Cost: {self.__cost}")
        print(f"Premium Amount: {self.__premium_amount}")

# Example usage
try:
    vehicle1 = Vehicle()
    vehicle1.set_vehicle_id("V101")
    vehicle1.set_vehicle_type("Two Wheeler")
    vehicle1.set_cost(50000)
    vehicle1.calculate_premium()
    vehicle1.display_vehicle_details()

    print("\n")

    vehicle2 = Vehicle()
    vehicle2.set_vehicle_id("V102")
    vehicle2.set_vehicle_type("Four Wheeler")
    vehicle2.set_cost(800000)
    vehicle2.calculate_premium()
    vehicle2.display_vehicle_details()

    print("\n")

    vehicle3 = Vehicle()
    vehicle3.set_vehicle_id("V103")
    vehicle3.set_vehicle_type("Invalid Type")
    vehicle3.set_cost(300000)
    vehicle3.calculate_premium()
    vehicle3.display_vehicle_details()

except ValueError as e:
    print(e)
