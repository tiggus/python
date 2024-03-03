from Car import Car
from CarRentalCompany import *
import threading
from Criteria import Criteria

class CarRentalTest:
    cars = [
        Car("Toyota", "RAV4", "NHK 337P", "B2", 90),
        Car("BMW", "X3", "NHK 338P", "C1", 90),
        Car("BMW", "X5", "NHK 339P", "A1", 90),
        Car("Ford", "Fiesta", "NHK 340P", "A1", 90)
    ]
   
def main():
    rental_company = CarRentalTest()
    
    all_cars = CarRentalCompany.matching_cars(rental_company, Criteria.make_criteria)
    print('\nall cars:')
    for car in all_cars:
        print(f"{car.make} {car.model}")

    matched_cars = CarRentalCompany.find_matching_cars(rental_company, Criteria.make_criteria)
    print('\nmatched cars:')
    for car in matched_cars:
        print(f"{car.make} {car.model}")
        
if __name__ == "__main__":
    main()
