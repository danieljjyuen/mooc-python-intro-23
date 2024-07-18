# Write your solution here
def add_entry(finnish:str, english:str):
    with open("dictionary.txt", "a") as main:
        main.write(f"{finnish} - {english}\n")

def search_entry(text:str):
    with open("dictionary.txt") as main:
        result = []
        for lines in main:
            lines = lines.strip()
            if text in lines:
                result.append(lines)
    return result

while True:
    print("1 - Add word, 2- Search, 3 - Quit")
    opt = int(input("Function:"))
    if opt == 3:
        print("Bye!")
        break
    elif opt == 1:
        finnish = input("The word in Finnish:")
        english = input("The word in English:")
        add_entry(finnish, english)
        print("Dictionary entry added")
    elif opt == 2:
        search = input("Search term:")
        list = search_entry(search)
        for item in list:
            print(item)

