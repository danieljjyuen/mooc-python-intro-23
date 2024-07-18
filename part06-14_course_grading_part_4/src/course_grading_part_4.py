file1 = input("Student information:")
file2 = input("Exercises completed:")
file3 = input("Exam points:")
file4  = input("Course information:")
# file1 = "students1.csv"
# file2 = "exercises1.csv"
dict = {}

with open(file4) as file_main4:
    lines = file_main4.readlines()
    line1 = lines[0]
    line2 = lines[1]
    line1 = line1.strip()
    part1 = line1.split(" ")

    title = ""
    for i in range(1, len(part1)):
        if len(title) == 0:
            title+= part1[i]
        else:
            title+=" "+part1[i]    
    line2 = line2.strip()
    part2 = line2.split(" ")
    title+=", "+part2[-1] + " credits\n"

    with open("results.txt", "w") as filemain5:
        filemain5.write(title)
        filemain5.write(f"{"="*(len(title)-1)}\n")



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
    
with open("results.txt", "a") as file_main6:
    file_main6.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}grade\n")
    for student in dict:
        exec_nbr = sum(dict[student]["courses"])
        exec_points = ((exec_nbr/40)*100)//10
        exm_pts = sum(dict[student]["exampoints"])
        tot_pts = exec_points + exm_pts
        finalgrade = grade(tot_pts)
        name = dict[student]["first"]+" "+dict[student]["last"]
        #file_main6.write(f"{dict[student]["first"]} {dict[student]["last"]} {finalgrade}\n")
        file_main6.write(f"{name:30}{exec_nbr:<10}{int(exec_points):<10}{exm_pts:<10}{int(tot_pts):<10}{finalgrade}\n")
with open("results.csv", "w") as file_main7:
    for student in dict:
        points = ((sum(dict[student]["courses"])/40)*100)//10 + sum(dict[student]["exampoints"])
        finalgrade = grade(points)
        file_main7.write(f"{student};{dict[student]["first"]} {dict[student]["last"]};{finalgrade}\n")

print("Results written to files results.txt and results.csv")