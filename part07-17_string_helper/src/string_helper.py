# Write your solution here
import string
def change_case(orig_string:str):
    word=""
    for char in orig_string:
        if char.isupper():
            word+= char.lower()
        else:
            word+= char.upper()
    return word
def split_in_half(orig_string:str):
    length = len(orig_string)//2
    return (orig_string[0:length], orig_string[length:])

def remove_special_characters(orig_string:str):
    choice = " "
    choice+=string.ascii_letters
    choice+=string.digits

    changed=""
    for char in orig_string:
        if char in choice:
            changed+=char
    return changed
