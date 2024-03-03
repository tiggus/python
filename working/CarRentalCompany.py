from Criteria import Criteria

class CarRentalCompany:
    def __init__(self):
        pass
    def matching_cars(self, make_criteria):
        return self.cars

    def find_matching_cars(self, make_criteria):
        matched_cars = []
        for car in self.cars:
            if make_criteria(car):
                matched_cars.append(car)
        return matched_cars