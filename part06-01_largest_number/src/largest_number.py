# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            current = int(line)
            if largest < current:
                largest = current
    return largest
