# Write your solution here
list = [1,2,3,4,5]

while True:

    ask = int(input("Index:"))
    if ask == -1:
        break
    newint = int(input("New value:"))
    list[ask] = newint
    print(list)
