
# Car Registration System
# This system is designed to register cars and their owners. It allows the user to add, update, and delete car records.
# The system also provides the functionality to search for a car by its registration number and display all registered cars.

class Car:
    def __init__(self, reg_no, make, model, owner):
        self.reg_no = reg_no
        self.make = make
        self.model = model
        self.owner = owner

    def display_car_info(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Owner: {self.owner}")
        print(self.owner, self.make, self.model, self.reg_no)

class CarRegistrationSystem:
    def __init__(self):
        self.cars = []


    def add_car(self, car):
        self.cars.append(car)
        print("Car added successfully!")

    def update_car(self, reg_no, make, model, owner):
        for car in self.cars:
            if car.reg_no == reg_no:
                car.make = make
                car.model = model
                car.owner = owner
                print("Car updated successfully!")
                return
        print("Car not found!")

    def delete_car(self, reg_no):
        for car in self.cars:
            if car.reg_no == reg_no:
                self.cars.remove(car)
                print("Car deleted successfully!")
                return
        print("Car not found!")

    def search_car(self, reg_no):
        for car in self.cars:
            if car.reg_no == reg_no:
                car.display_car_info()
                return
        print("Car not found!")

    def display_all_cars(self):
        if self.cars:
            for car in self.cars:
                car.display_car_info()
                
                
        else:
            print("No cars registered yet.")

#Includes polymorphism by overriding or overloading methods. For example, I can create a Truck class that inherits from the Car class and overrides the display_car_info method to display additional information specific to trucks.

class Truck(Car):
    def __init__(self, reg_no, make, model, owner, capacity):
        super().__init__(reg_no, make, model, owner)
        self.capacity = capacity


    def  display_car_info(self):
        super().display_car_info()
        print(f"Capacity: {self.capacity}")

        
#Includes encapsulation by making the car attributes private and providing getter and setter methods to access and modify them. For example, you can make the reg_no attribute private and provide a get_reg_no method to retrieve the registration number.

class Car:
    def __init__(self, reg_no, make, model, owner):
        self.__reg_no = reg_no
        self.make = make
        self.model = model
        self.owner = owner

    def get_reg_no(self):
        return self.__reg_no

    def set_reg_no(self, reg_no):
        self.__reg_no = reg_no

#Includes inheritance by creating a Vehicle class that contains common attributes and methods shared by cars and trucks. The Car and Truck classes can then inherit from the Vehicle class to reuse the common functionality.

class Vehicle:
    def __init__(self, reg_no, make, model, owner):
        self.reg_no = reg_no
        self.make = make
        self.model = model
        self.owner = owner

    def display_vehicle_info(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Owner: {self.owner}")

class Car(Vehicle):
    def __init__(self, reg_no, make, model, owner):
        super().__init__(reg_no, make, model, owner)

class Truck(Vehicle):
    def __init__(self, reg_no, make, model, owner, capacity):
        super().__init__(reg_no, make, model, owner)
        self.capacity = capacity

    def display_vehicle_info(self):
        super().display_vehicle_info()
        print(f"Capacity: {self.capacity}")

class truckRegistrationSystem(CarRegistrationSystem):
    def __init__(self):
        super().__init__()

    def add_truck(self, truck):
        self.cars.append(truck)
        print("Truck added successfully!")

    def update_truck(self, reg_no, make, model, owner, capacity):
        for truck in self.cars:
            if truck.reg_no == reg_no:
                truck.make = make
                truck.model = model
                truck.owner = owner
                truck.capacity = capacity
                print("Truck updated successfully!")
                return
        print("Truck not found!")

    def delete_truck(self, reg_no):
        for truck in self.cars:
            if truck.reg_no == reg_no:
                self.cars.remove(truck)
                print("Truck deleted successfully!")
                return
        print("Truck not found!")

    def search_truck(self, reg_no):
        for truck in self.cars:
            if truck.reg_no == reg_no:
                truck.display_vehicle_info()
                return
        print("Truck not found!")

    def display_all_trucks(self):
        if self.cars:
            for truck in self.cars:
                truck.display_vehicle_info()
        else:
            print("No trucks registered yet.")

        
               
          
# Main Program
print("Do you want to register a car or a truck?")
print("1. Car")
print("2. Truck")
choice = input("Enter your choice: ")


car_system = CarRegistrationSystem()

while choice=='1':
    print("Car Registration System")
    print("1. Add Car")
    print("2. Update Car")
    print("3. Delete Car")
    print("4. Search Car")
    print("5. Display All Cars")
    print("6. Exit")
  


    choice = input("Enter your choice: ")

    if choice == '1':
        reg_no = input("Enter Registration Number: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        owner = input("Enter Owner: ")
        capacity = input("Enter Capacity: ")
        car = Car(reg_no, make, model, owner)
        truck= Truck(reg_no, make, model, owner, capacity)
        car_system.add_car(car)
        car_system.add_car(truck)

    elif choice == '2':
        reg_no = input("Enter Registration Number: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        owner = input("Enter Owner: ")
        car_system.update_car(reg_no, make, model, owner)

    elif choice == '3':
        reg_no = input("Enter Registration Number: ")
        car_system.delete_car(reg_no)

    elif choice == '4':
        reg_no = input("Enter Registration Number: ")
        car_system.search_car(reg_no)

    elif choice == '5':
        car_system.display_all_cars()



    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
   
    print()
  
truck_system = truckRegistrationSystem()

while choice=='2':

    print("Truck Registration System")
    print("1. Add Truck")
    print("2. Update Truck")
    print("3. Delete Truck")
    print("4. Search Truck")
    print("5. Display All Trucks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        reg_no = input("Enter Registration Number: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        owner = input("Enter Owner: ")
        capacity = input("Enter Capacity: ")
        truck = Truck(reg_no, make, model, owner, capacity)
        truck_system.add_truck(truck)

    elif choice == '2':
        reg_no = input("Enter Registration Number: ")
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        owner = input("Enter Owner: ")
        capacity = input("Enter Capacity: ")
        truck_system.update_truck(reg_no, make, model, owner, capacity)

    elif choice == '3':
        reg_no = input("Enter Registration Number: ")
        truck_system.delete_truck(reg_no)

    elif choice == '4':
        reg_no = input("Enter Registration Number: ")
        truck_system.search_truck(reg_no)

    elif choice == '5':
        truck_system.display_all_trucks()

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

    print()


    


    





