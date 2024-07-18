# Write your solution here
def same_chars(text, num, num2):
    length = len(text)
    if num >= length or num2 >= length:
        return False
    return text[num] == text[num2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))

