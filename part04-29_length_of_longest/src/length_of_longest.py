# Write your solution here

def length_of_longest(list):
    length =0
    for i in list:
        if length <= len(i):
            length = len(i)

    return length