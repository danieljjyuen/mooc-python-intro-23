# write your solution here
file1 = input("Student information:")
file2 = input("Exercises completed:")
file3 = input("Exam points:")
# file1 = "students1.csv"
# file2 = "exercises1.csv"
dict = {}

with open(file1) as file_main1:
    for line in file_main1:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        dict[parts[0]] = {
            "first" : parts[1],
            "last": parts[2],
            "courses": [],
            "exampoints":[]
        }

with open(file2) as file_main2:
    for line in file_main2:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        lists = list(map(int, parts[1:]))
        dict[parts[0]]["courses"].extend(lists)

with open(file3) as file_main3:
    for line in file_main3:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        lists = list(map(int, parts[1:]))
        dict[parts[0]]["exampoints"].extend(lists)

def grade(number):
    if number<=14:
        return 0
    elif number <=17:
        return 1
    elif number <=20:
        return 2
    elif number<= 23:
        return 3
    elif number<= 27:
        return 4
    else:
        return 5
for student in dict:
    # print(student)
    #print(f"{dict[student]["first"]} {dict[student]["last"]} {sum(dict[student]["courses"])}")
    points = ((sum(dict[student]["courses"])/40)*100)//10 + sum(dict[student]["exampoints"])
    #print(f"first {sum(dict[student]["courses"])}  {sum(dict[student]["exampoints"])}")
    finalgrade = grade(points)
    print(f"{dict[student]["first"]} {dict[student]["last"]} {finalgrade}")