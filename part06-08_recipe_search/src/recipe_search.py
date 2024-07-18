# Write your solution here


           

def search_by_name(filename:str, word:str):
    dic = dictionary(filename)
    lists = []
    for i in dic:
        if word in i.lower():
            lists.append(i.strip())
    return lists

def search_by_time(filename:str, prep_time:int):
    dic = dictionary(filename)
    lists = []
    for i in dic:
        if prep_time >= dic[i]["prep"]:
            # print(f"{i}, preparation time {dic[i]["prep"]} min")
            lists.append(f"{i}, preparation time {dic[i]["prep"]} min")
    return lists


def search_by_ingredient(filename:str, ingredient:str):
    dic = dictionary(filename)
    lists = []
    for i in dic:
        list = dic[i]["ingre"]
        if ingredient in list:
            #print(f"{i}, preparation time {dic[i]["prep"]} min")
            lists.append(f"{i}, preparation time {dic[i]["prep"]} min")
    return lists

def dictionary(filename:str):
    with open(filename) as file_main:
        dictionaryx = {}
        lines = file_main.readlines()
        i = 0
        while i< len(lines):
            name = lines[i].strip()
            i+=1
            prep = int(lines[i].strip())
            i+=1
            ingre = []
            while i < len(lines) and lines[i].strip() != "":
                ingre.append(lines[i].strip())
                i+=1
            dictionaryx[name] = {
                "prep": prep,
                "ingre":ingre
            }
            i+=1
    return dictionaryx
#search_by_time("recipes1.txt", 20)
#print(search_by_name("recipes1.txt", "cake"))
# print(dictionary("recipes1.txt"))
# search_by_ingredient("recipes1.txt", "eggs")
