def add_student(database, name:str):
    database[name] = {}

def print_student(database, name:str):
    if name not in database:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        if len(database[name]) ==0:
            print(" no completed courses")
        else:
            print(f" {len(database[name])} completed courses:")
            summ =0
            for course in database[name]:
                print(f"  {course} {database[name][course]}")
                summ+= database[name][course]
            print(f" average grade { summ / len(database[name]):.1f}")

def add_course(database, name:str, course):
    if course[1] == 0:
        return
    if course[0] in database[name]:
        current = database[name][course[0]]
        if current < course[1]:
            database[name][course[0]] = course[1]
    else:
        database[name][course[0]] = course[1]

def summary(database):
    print(f"students {len(database)}")
    maxcourse = 0
    maxperson =""

    bestavg =0
    bestperson =""

    for person in database:
        numberofcourse = len(database[person])
        if numberofcourse >= maxcourse:
            maxcourse = numberofcourse
            maxperson = person
        
        summ=0
        for course in database[person]:
            summ+= database[person][course]
        
        currentavg = summ / numberofcourse
        if bestavg <= currentavg:
            bestavg = currentavg
            bestperson = person
    
    print(f"most courses completed {maxcourse} {maxperson}")
    print(f"best average grade {bestavg} {bestperson}")

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)