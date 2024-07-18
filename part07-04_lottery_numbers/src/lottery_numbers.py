# Write your solution here
from random import randint
def lottery_numbers(amount:int, lower:int, upper:int):
    list = []

    while len(list) < amount:
        number = randint(lower, upper)
        if number not in list:
            list.append(number)
    
    list.sort()
    return list

#print(lottery_numbers(7, 1, 10))