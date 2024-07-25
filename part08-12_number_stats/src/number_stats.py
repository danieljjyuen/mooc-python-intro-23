# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0
    def add_number(self, number:int):
        self.numbers+=1
        self.sum += number
    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.sum
    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum()/self.count_numbers()


obj = NumberStats()
even = NumberStats()
odd = NumberStats()
print("Please type in a integer numbers:")
while True:
    number = int(input(""))
    if number == -1:
        print(f"Sum of numbers: {obj.get_sum()}")
        print(f"Mean of numbers: {obj.average()}")
        print(f"Sum of even numbers: {even.get_sum()}")
        print(f"Sum of odd numbers: {odd.get_sum()}")
        break
    else:
        obj.add_number(number)
        if number %2 ==0:
            even.add_number(number)
        else:
            odd.add_number(number)

    

