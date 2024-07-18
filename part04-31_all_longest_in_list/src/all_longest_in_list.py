# Write your solution here
def all_the_longest(lists):
    greatest = max(len(s) for s in lists)
    newlist = []
    for i in lists:
        if len(i) == greatest:
            newlist.append(i)
    return newlist
