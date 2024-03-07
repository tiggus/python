from main.rental.Criteria import Criteria
from main.rental.Car import Car
import threading

# filter = Criteria('BMW')
# print('filtermake:', filter.make_criteria() )

class CarRentalCompany:
    def __init__(self):
        self.lock = threading.Lock()
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def matching_cars(self, criteria):
        return self.cars
    
    def find_matching_cars(self, make_criteria):
        matched_cars = []
        with self.lock:
            for car in self.cars:
                if make_criteria(car):
                    matched_cars.append(car)
            return matched_cars

    def rent_car(self, renter, car):
        pass

    def return_car(self, renter, car):
        pass
