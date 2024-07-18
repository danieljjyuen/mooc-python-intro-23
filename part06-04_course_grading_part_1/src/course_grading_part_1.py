# write your solution here
file1 = input("Student information:")
file2 = input("Exercises completed:")

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
            "courses": []
        }

with open(file2) as file_main2:
    for line in file_main2:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        lists = list(map(int, parts[1:]))
        dict[parts[0]]["courses"].extend(lists)

for student in dict:
    # print(student)
    print(f"{dict[student]["first"]} {dict[student]["last"]} {sum(dict[student]["courses"])}")