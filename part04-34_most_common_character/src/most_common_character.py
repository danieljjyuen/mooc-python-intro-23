# Write your solution here
def most_common_character(first):
    letter =""
    count=0
    for i in first:
        if( count < first.count(i)):
            count = first.count(i)
            letter = i
    return letter