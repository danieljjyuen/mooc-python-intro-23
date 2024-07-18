# Write your solution here
def no_shouting(list):
    newlist =[]
    for i in list:
        if not i.isupper():
            newlist.append(i)
    return newlist