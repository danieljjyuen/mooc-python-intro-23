# Write your solution here

def add_diary(sentence:str):
    with open("diary.txt", "a") as file:
        file.write(f"{sentence}\n")

def read_diary():
    with open("diary.txt") as file:
        print("Entries:")
        for line in file:
            print(line.strip())

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    opt = int(input("Function:"))
    if opt == 0:
        print("Bye now!")
        break
    elif opt == 1:
        sentence = input("Diary entry:")
        add_diary(sentence)
        print("Diary saved")
    elif opt == 2:
        read_diary()
            
