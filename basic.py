# class Criteria:
#     pass
# #     def __init__(self, make):
# #         self.make = make
# #         self.cars = []
# #     def make_criteria(self):
# #         return self.make
# #         #return self.make == 'BMW'

class Car:
    count = 0
    def __init__(self, make, model, registration_number, rental_group, cost_per_day):
        self.make = make
        self.model = model
        self.registration_number = registration_number
        self.rental_group = rental_group
        self.cost_per_day = cost_per_day
        self.count += 1
    
# class CarRentalCompany:
#     def __init__(self):
#         self.cars = [
#             Car("Toyota", "RAV4", "NHK 337P", "B2", 90),
#             Car("BMW", "X3", "NHK 338P", "C1", 90),
#             Car("BMW", "X5", "NHK 339P", "A1", 90),
#             Car("Ford", "Fiesta", "NHK 340P", "A1", 90)
#         ]
#     def matching_cars(self, criteria):
#         return self.cars
    
#     # def find_matching_cars(self, criteria):
#     #     matching_cars = []
#     #     for car in self.cars:
#     #         if criteria(car):
#     #             matching_cars.append(car)
#     #     return matching_cars
    

# def main():
#     all_cars = CarRentalCompany.matching_cars(CarRentalCompany, Criteria)
#     print('\nall cars:')
#     for car in all_cars:
#         print(f"{car.make} {car.model}")

#     # for car in matching_cars:
#     #     print(f"{car.make} {car.model}")

# if __name__ == "__main__":
#     main()




# # filter = Criteria('BMW')
# # print('filtermake:', filter.make_criteria() )



        
# # all_cars = CarRentalCompany.matching_cars(rental_company, Criteria.make_criteria)
# # print('\nall cars:')
# # for car in all_cars:
# #     print(f"{car.make} {car.model}")

# # matched_cars = CarRentalCompany.find_matching_cars(rental_company, filter.make_criteria())
# # print('\nmatched cars:')
# # for car in matched_cars:
# #     print(f"{car.make} {car.model}")


