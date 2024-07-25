# Write your solution here
def smallest_average(person1:dict, person2:dict, person3:dict):
    p1 = (person1["result1"]+person1["result2"]+person1["result3"])/3
    p2 = (person2["result1"]+person2["result2"]+person2["result3"])/3
    p3 = (person3["result1"]+person3["result2"]+person3["result3"])/3

    smallest = min(p1,p2,p3)

    if smallest == p1:
        return person1
    elif smallest == p2:
        return person2
    else:
        return person3