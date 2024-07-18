# Write your solution here
def histogram(input):
    dict = {}
    for i in input:
        if i not in dict:
            dict[i] =1
        else:
            dict[i] += 1

    for i in dict:
        print(f"{i} {"*" * dict[i]}")