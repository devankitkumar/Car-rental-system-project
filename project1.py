class Car:
    def __init__(self, car_id, make, model, year, mileage, available=True):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available

class CarRentalSystem:
    def __init__(self):
        self.cars = {}

    def add_car(self, car_id, make, model, year, mileage):
        if car_id not in self.cars:
            self.cars[car_id] = Car(car_id, make, model, year, mileage)
            print(f"Car {car_id} added successfully.")
        else:
            print("Car ID already exists.")

    def remove_car(self, car_id):
        if car_id in self.cars:
            del self.cars[car_id]
            print(f"Car {car_id} removed successfully.")
        else:
            print("Car ID not found.")

    def rent_car(self, car_id):
        if car_id in self.cars:
            if self.cars[car_id].available:
                self.cars[car_id].available = False
                print(f"Car {car_id} rented successfully.")
            else:
                print("Car is not available for rent.")
        else:
            print("Car ID not found.")

    def return_car(self, car_id, mileage):
        if car_id in self.cars:
            if not self.cars[car_id].available:
                self.cars[car_id].available = True
                self.cars[car_id].mileage += mileage
                print(f"Car {car_id} returned successfully.")
            else:
                print("Car is already available.")
        else:
            print("Car ID not found.")

    def display_available_cars(self):
        available_cars = [car for car in self.cars.values() if car.available]
        if available_cars:
            print("Available Cars:")
            for car in available_cars:
                print(f"ID: {car.car_id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage}")
        else:
            print("No cars available.")

# Sample usage
if __name__ == "__main__":
    rental_system = CarRentalSystem()
    rental_system.add_car(1, "Toyota", "Corolla", 2020, 5000)
    rental_system.add_car(2, "Honda", "Civic", 2019, 6000)
    rental_system.rent_car(1)
    rental_system.display_available_cars()
