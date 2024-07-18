# Write your solution here

dict = {}
while True:
    option = int(input("command(1 search, 2 add, 3 quit):"))
    if option == 1:
        askname = input("name:")
        if askname in dict:
            for i in dict[askname]:
                print(i)
        else:
            print("no number")
    elif option == 2:
        name = input("name:")
        number = input("number:")
        if name not in dict:
            dict[name] = [number]
        else:
            dict[name].append(number)

        print("ok!")
    elif option == 3:
        print("quitting...")
        break