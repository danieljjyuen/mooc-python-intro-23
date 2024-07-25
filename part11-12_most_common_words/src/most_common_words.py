# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename:str, lower_limit:int):
    with open(filename) as file_main:
        words = []
        for lines in file_main:
            lines = lines.strip().split(" ")
            for word in lines:
                words.append("".join(ch for ch in word if ch in string.ascii_lowercase))
        

    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))