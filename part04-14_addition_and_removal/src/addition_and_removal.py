# Write your solution here
number =1
list =[]
print(f"The list is now []")
while True:

    word = input("a(d)d, (r)emove or e(x)it:")

    if word == "x":
        print("Bye!")
        break
    elif word == "d":
        list.append(number)
        number+=1
    else:
        list.pop(-1)
        number-=1  
    print(f"The list is now {list}")