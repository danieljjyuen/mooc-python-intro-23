# Write your solution here
def shortest(list):
    length = len(list[0])
    word = list[0]
    for i in list:
        if length >= len(i):
            length = len(i)
            word = i
    return word