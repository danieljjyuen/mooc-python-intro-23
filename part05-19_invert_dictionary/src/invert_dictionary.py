# Write your solution here
def invert(dictionary:dict):
    list =[]
    for i in dictionary:
        list.append(i)
    for i in list:
        dictionary[dictionary[i]] = i
        del dictionary[i]

#invert({1: 10, 2: 20, 3: 30})
    