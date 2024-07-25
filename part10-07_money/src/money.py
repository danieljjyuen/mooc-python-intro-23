# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __get_total(self):
        return (self.__euros*100) + self.__cents
    
    def __eq__(self, another):
        selftotal = self.__get_total()
        anothertotal = another.__get_total()
        return selftotal == anothertotal
    
    def __ne__(self, another):
        return self.__get_total() != another.__get_total()
    
    def __gt__(self, another):
        return self.__get_total() > another.__get_total()
    
    def __lt__(self, another):
        return self.__get_total() < another.__get_total()
    
    def __add__(self, another):
        total = self.__get_total() + another.__get_total()

        return Money(total//100, total%100)
    
    def __sub__(self, another):
        if another > self:
            raise ValueError(f"a negative result is not allowed")
        total = self.__get_total() - another.__get_total()
        return Money(total//100, total%100)
    

