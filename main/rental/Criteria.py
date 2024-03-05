class Criteria:
    def __init__(self, make):
        self.make = make
        self.cars = []
    def make_criteria(self):
        return self.make

# filter = Criteria('BMW')
# print('make:', filter.make_criteria())