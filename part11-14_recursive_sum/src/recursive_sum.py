# WRITE YOUR SOLUTION HERE:
def recursive_sum(number:int):
    if number <= 1:
        return 1
    
    else:
        return number + recursive_sum(number-1)