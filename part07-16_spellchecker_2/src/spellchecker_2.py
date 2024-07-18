import difflib

def wordlist():
    with open("wordlist.txt") as file_main:
        words = []
        for lines in file_main:
            lines = lines.strip()
            words.append(lines)
    return words

stored = wordlist()
sentence = input("write text:")
mistake = []
response=""
parts = sentence.split(" ")
for part in parts:
    lower = part.lower()
    if lower in stored:
        if len(response) == 0:
            response+=part
        else:
            response+=f" {part}"
    else:
        mistake.append(part)
        if len(response) ==0:
            response+=f"*{part}*"
        else:
            response+=f" *{part}*"
print(response)
    
if len(mistake) >0:
    print("suggestions:")
    for word in mistake:
        suggest = difflib.get_close_matches(word.lower(), stored)
        print(f"{word}: {", ".join(suggest)}")