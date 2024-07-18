# Write your solution here
def write_add(filename, sentence):
    with open(filename, "a") as file:
        file.write(sentence)

def filter_solutions():
    with open("correct.csv", "w") as my_file1:
        pass
    with open("incorrect.csv", "w") as my_file2:
        pass
    with open("solutions.csv") as file:
        for lines in file:
            lines = lines.strip()
            parts = lines.split(";")
            # print(eval(parts[1]))
            # print(parts[2])
            # print(eval(parts[1])== int(parts[2]))
            if eval(parts[1]) == int(parts[2]):
                write_add("correct.csv", lines+"\n")
            else:
                write_add("incorrect.csv", lines+"\n")

# filter_solutions()