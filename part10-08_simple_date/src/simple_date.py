# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __eq__(self, another):
        if self.__day != another.__day:
            return False
        if self.__month != another.__month:
            return False
        if self.__year != another.__year:
            return False
        return True
    
    def __ne__(self, another):
        return not self.__eq__(another)
    

    def __convert(self):
        return (self.__year *360 )+ (self.__month *30) + self.__day
    
    def __lt__(self, another):
        return self.__convert() < another.__convert()
    
    def __gt__(self, another):
        return self.__convert() > another.__convert()
    
    def __add__(self, another):
        newdays = self.__convert() + another

        return SimpleDate( (newdays%360)%30, (newdays%360)//30, newdays//360)
    
    def __sub__(self, another):
        return abs(self.__convert() - another.__convert())
    


