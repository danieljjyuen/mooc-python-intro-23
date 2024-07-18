# Write your solution here

dict = {}
while True:
    option = int(input("command(1 search, 2 add, 3 quit):"))
    if option == 1:
        askname = input("name:")
        if askname in dict:
            print(dict[askname])
        else:
            print("no number")
    elif option == 2:
        name = input("name:")
        number = input("number:")
        dict[name] = number
        print("ok!")
    elif option == 3:
        print("quitting...")
        break