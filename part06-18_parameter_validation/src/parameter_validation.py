# Write your solution here
def new_person(name:str, age:int):

    if name =="" or len(name) >=40 or " " not in name or age<0 or age >150:
        raise ValueError("value not valid")
    else:
        return (name, age)

