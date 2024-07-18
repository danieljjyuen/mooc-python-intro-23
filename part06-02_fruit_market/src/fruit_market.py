# write your solution here
def read_fruits():
    with open("fruits.csv") as file_main:
        dic = {}
        for line in file_main:
            parts = line.replace("\n", "").split(";")
            dic[parts[0]] = float(parts[1])
        
        return dic