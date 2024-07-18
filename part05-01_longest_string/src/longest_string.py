# Write your solution here
def longest(strings:list):
    great =0
    word=""
    for i in strings:
        if len(i) > great:
            great = len(i)
            word = i
    return word
