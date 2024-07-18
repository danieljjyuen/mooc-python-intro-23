# Write your solution here
import string
def separate_characters(my_string:str):
    part1 =""
    part2=""
    part3=""

    for letter in my_string:
        if letter in string.ascii_letters:
            part1+=letter
        elif letter in string.punctuation:
            part2+=letter
        else:
            part3+=letter
    return (part1, part2, part3)