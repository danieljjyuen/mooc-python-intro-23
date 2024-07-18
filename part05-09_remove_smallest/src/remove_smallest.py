# Write your solution here
def remove_smallest(numbers:list):
    small =numbers[0]
    for i in numbers:
        if small > i:
            small = i
    numbers.remove(small)