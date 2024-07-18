# Write your solution here
def palindromes(word:str):
    length1 = len(word)
    length = len(word)//2
    for i in range(length):
        if word[i] != word[length1-i-1]:
            #print("that wasn't a palindrome")
            return False
    #print(f"{word} is a palindrome!")
    return True

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
main()
# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
    
# block!

