# Write your solution here
def older_people(people:list, year:int):
    newlist = []
    for person in people:
        if person[1] <year:
            newlist.append(person[0])
    return newlist