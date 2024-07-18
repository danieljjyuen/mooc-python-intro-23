# Write your solution here
list = []

while True:
    word = int(input("New item:"))
    if word == 0:
        print("Bye!")
        break

    list.append(word)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")