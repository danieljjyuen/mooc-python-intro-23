# Write your solution here
import string
import random
def generate_strong_password(amount:int, number:bool, special:bool):
    pw=""

    while len(pw) <amount:
        if number and len(pw)<amount :
            pw+= f"{random.randint(0,9)}"
        
        if special and len(pw)<amount:
            pw+= random.choice("!?=+-()#")
        
        if len(pw) < amount:
            pw+= random.choice(string.ascii_lowercase)
    return pw
