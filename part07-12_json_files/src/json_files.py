# Write your solution here
import json

def print_persons(filename:str):
    with open(filename) as file_main:
        data = file_main.read()
        content = json.loads(data)
        for obj in content:
            
            print(f"{obj["name"]} {obj["age"]} years ({", ".join(obj["hobbies"])})")
#print_persons('file1.json')