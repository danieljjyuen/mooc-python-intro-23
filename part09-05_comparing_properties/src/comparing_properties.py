# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compare_to):
        return ( self.square_metres) > ( compare_to.square_metres)
    
    def price_difference(self, compared_to):
        return abs((self.square_metres*self.price_per_sqm)-
                   (compared_to.square_metres * compared_to.price_per_sqm))

    def more_expensive(self, compared_to):
        return (self.rooms*self.square_metres*self.price_per_sqm) > (compared_to.rooms * compared_to.square_metres * compared_to.price_per_sqm)
