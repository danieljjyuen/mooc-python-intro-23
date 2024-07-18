# Write your solution here
def everything_reversed(list) :
    newlist =[]
    length = len(list)
    for i in range(length-1, -1,-1):
        newlist.append(list[i][::-1])
    return newlist