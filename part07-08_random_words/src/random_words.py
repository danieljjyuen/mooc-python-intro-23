# Write your solution here
import random

def words(n:int, beginning:str):
    wordlist = []
    with open("words.txt") as file_main:
        for lines in file_main:
            lines = lines.strip()
            #print(lines)
            if lines.startswith(beginning):
                wordlist.append(lines)
    if len(wordlist) <n:
        raise ValueError
    returnlist = []
    
    while len(returnlist)  < n:
        wd = random.choice(wordlist)
        if wd not in returnlist:
            returnlist.append(wd)
    
    if len(returnlist)!=n:
        raise ValueError
        
    return returnlist

# print(words(10, "fasdfa"))