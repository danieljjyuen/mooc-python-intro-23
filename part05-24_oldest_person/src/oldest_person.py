# Write your solution here
def oldest_person(people:list):
    currentyear =people[0][1]
    currentname = people[0][0]

    for i in people:
        if i[1] < currentyear:
            currentyear = i[1]
            currentname = i[0]
    return currentname