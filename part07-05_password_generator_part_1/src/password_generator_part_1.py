# Write your solution here
import random
import string
def generate_password(amount:int):
    pw =""
    for i in range(amount):
        pw+= random.choice(string.ascii_lowercase)
    return pw