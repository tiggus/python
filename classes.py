from main.rental.Car import *
from main.rental.CarRentalCompany import *
from main.rental.Criteria import *
from main.utils.DatePeriod import *
from main.utils.DatePeriodUtil import *
import sys, inspect

# def print_classes():
#     for name, obj in inspect.getmembers(sys.modules[__name__]):
#         if inspect.isclass(obj):
#             print(obj)

def print_classes():
    current_module = sys.modules[__name__]
    keys = []
    for key in dir(current_module):
        if isinstance( getattr(current_module, key), type ):
            print(key)
            keys.append(key)
    return keys
classes = print_classes()
print('\t',classes[3])
print(classes)

#print(classes)

# for name, obj in inspect.getmembers(CarRentalCompany):
#     if inspect.isclass(obj):
#         print(obj)
# if classes is not None:
#     counter = 0
#     for cla in classes:
#         counter =+ 1
#         #print([counter], [cla])
#         for item in [cla].__dict__:
#             print (item, ':', [cla].__dict__[item])