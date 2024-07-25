# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person:Person):
        self.persons.append(person)

    def is_empty(self):
        if len(self.persons) ==0:
            return True
        else:
            return False
    def print_contents(self):
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        if self.is_empty():
            return None
        
        # name = self.persons[0].name
        height = self.persons[0].height
        per = self.persons[0]
        for person in self.persons:
            if person.height < height:
                height = person.height
                # name = person.name
                per = person
        
        return per
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        
        per = self.shortest()
        self.persons.remove(per)

        # result = None
        # for person in self.persons:
        #     if person.name == name:
        #         result = person
        #         break
        
        # self.persons.remove(result)
        # return result
        return per
