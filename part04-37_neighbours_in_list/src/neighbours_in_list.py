# Write your solution here
def longest_series_of_neighbours(list):
    count =1
    greatest =0
    for i in range(1, len(list)):
        if abs(list[i]-list[i-1]) ==1:
            count+=1
            if count > greatest:
                greatest = count
        else:
            count =1
    return greatest