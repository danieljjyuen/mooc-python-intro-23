class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
      
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    

class Suitcase:
    def __init__(self, max):
        self.__max = max
        self.__items = []
        self.__current = 0

    def max(self):
        return self.__max
    
    def items(self):
        return self.__items
    
    def current(self):
        return self.__current
    
    def add_item(self, item):

        if (self.__current + item.weight()) <= self.__max:
            self.__items.append(item)
            self.__current+= item.weight()
    
    def __str__(self):
        if len(self.items()) != 1:
            return f"{len(self.__items)} items ({self.__current} kg)"
        else:
            return f"{len(self.__items)} item ({self.__current} kg)"
    

    def print_items(self):
        for item in self.__items:
            print(item)
    
    def weight(self):
        return self.__current
    
    def heaviest_item(self):
        result = None
        if len(self.__items) == 0:
            return result
        
        currentmax = 0

        for item in self.__items:
            if item.weight() > currentmax:
                currentmax = item.weight()
                result = item
        return result
    
class CargoHold:
    def __init__(self, max):
        self.__max = max
        self.__items = []
        self.__current = 0

    def max(self):
        return self.__max
    
    def items(self):
        return self.__items
    
    def current(self):
        return self.__current
    
    def add_suitcase(self, suitcase):
        if self.__current + suitcase.weight() <= self.__max:
            self.__items.append(suitcase)
            self.__current+= suitcase.weight()

    def __str__(self):
        if len(self.__items) != 1:
            return f"{len(self.__items)} suitcases, space for {self.__max - self.__current} kg"
        return f"{len(self.__items)} suitcase, space for {self.__max - self.__current} kg"
    
    def print_items(self):
        for suitcase in self.__items:
            for item in suitcase.items():
                print(item)
