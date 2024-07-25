class LotteryNumbers:
    def __init__(self, weeks:int, seven:list):
        self.weeks = weeks
        self.seven = seven
    
    def number_of_hits(self, numbers:list):
        return len([number for number in numbers if number in self.seven])
    
    def hits_in_place(self, numbers):
        return [number if number in self.seven else -1 for number in numbers]