import random

class Car:
    def __init__(self, car_id, make, model, year, mileage, available):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available

class CarRentalSystem:
    def __init__(self):
        self.cars = {}

    def add_car(self):
        car_id = input("Enter car ID: ")
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = int(input("Enter car year: "))
        mileage = int(input("Enter car mileage: "))
        available = random.choice([True, False])
        self.cars[car_id] = Car(car_id, make, model, year, mileage, available)
        print(f"Car {car_id} added successfully.")

    def display_cars(self):
        for car in self.cars.values():
            availability = "available" if car.available else "rented"
            print(f"ID: {car.car_id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage}, Availability: {availability}")

# Sample usage
if __name__ == "__main__":
    rental_system = CarRentalSystem()
    num_cars = int(input("Enter the number of cars to add: "))
    for _ in range(num_cars):
        rental_system.add_car()
    
    print("\nCars in the system:")
    rental_system.display_cars()
