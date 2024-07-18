# Write your solution here
def formatted(listt) :
    newlist = []
    for i in listt:
        newlist.append(f"{i:.2f}")
    return newlist