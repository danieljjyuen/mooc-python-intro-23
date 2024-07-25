# Write your solution here
import re

def is_dotw(my_string:str):
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string:str):
    for letter in my_string:
        if re.search("[aeiouAEIOU]",letter):
            continue
        else:
            return False
    return True

def time_of_day(my_string:str):
    return bool(re.fullmatch("([0-1][0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9]", my_string))
 