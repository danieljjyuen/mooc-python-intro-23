# Write your solution here
def makelist():
    lis = []
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            lis.append(line)
    return lis
def find_words(search_term:str):
    currentlist = makelist()
    result = []
    if "." not in search_term and "*" not in search_term:
        for word in currentlist:
            if search_term ==  word:
                result.append(word)

    elif "*" in search_term:
        if "*" == search_term[0]:
            for word in currentlist:
                if word.endswith(search_term[1:]):
                    result.append(word)
        else:
            for word in currentlist:
                if word.startswith(search_term[:-1]):
                    result.append(word)
    elif "." in search_term:
        length = len(search_term)
        for word in currentlist:
            flag = True
            if len(word) == length:
                for num in range(length):
                    if search_term[num] == "." or search_term[num] == word[num]:
                        continue
                    elif search_term[num] != word[num]:
                        flag = False
                        break
            else:
                flag = False
            if flag == True:
                result.append(word)
    return result