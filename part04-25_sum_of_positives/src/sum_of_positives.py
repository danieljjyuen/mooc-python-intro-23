# Write your solution here
def sum_of_positives(list):
    summ = 0
    for i in list:
        if i > 0:
            summ+=i
    return summ
