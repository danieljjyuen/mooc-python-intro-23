# Write your solution here
import random

def roll(die:str):
    diea = [3,3,3,3,3,6]
    dieb = [2,2,2,5,5,5]
    diec = [1,4,4,4,4,4]

    if die == "A":
        return random.choice(diea)
    elif die == "B":
        return random.choice(dieb)
    elif die=="C":
        return random.choice(diec)

def play(die1:str, die2:str, times:int):
    win1=0
    win2=0
    tie=0


    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if result1 > result2:
            win1+=1
        elif result1 < result2:
            win2+=1
        else:
            tie+=1

    return (win1, win2, tie)