# write your solution here
ask = input("Write text:")

dic = []
with open("wordlist.txt") as file_main:
    for line in file_main:
        line = line.strip()
        dic.append(line)

words = ask.split(" ")
rebuild =""
for word in words:
    lower = word.lower()
    if lower in dic:
        if len(rebuild) ==0:
            rebuild+= word
        else:
            rebuild+= " "+word
    else:
        if len(rebuild) ==0:
            rebuild+= "*"+word+"*"
        else:
            rebuild+=" *"+word+"*"

print(rebuild)