# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial = initial_value
    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value ==0:
            pass
        else:
            self.value -=1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial
    # Write the rest of the methods here!
     

    
