# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self,name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.weight=0
        self.list = []

    def add_present(self, present:Present):
        self.list.append(present)
        self.weight+= present.weight
    
    def total_weight(self):
        return self.weight
