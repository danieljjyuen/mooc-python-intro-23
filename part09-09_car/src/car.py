# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__amount =0
        self.__odometer =0

    def fill_up(self):
        self.__amount = 60

    def drive(self, km:int):

        if self.__amount < km:
            self.__amount = 0
        else:
            self.__amount -= km
            self.__odometer += km
    
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount} litres"
    

# car = Car()
# car.drive(10)
# car.drive(20)
# car.drive(10)
# car.drive(20)
# car.drive(5)
# car.fill_up()
# car.drive(10)
# print(car)