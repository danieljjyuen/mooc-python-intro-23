class Application:
    def __init__(self):
        self.__record = Record()
    
    def helper(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credit: "))
        self.__record.add_course(Course(name, grade, credit))

    def get_course(self):
        name = input("course: ")
        return self.__record.get_by_name(name)
        
    def statistic(self):
        self.__record.statistic()

    def execute(self):
        self.helper()

        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()

            elif command == "2":
                data = self.get_course()
                if data == None:
                    print("no entry for this course")
                else:
                    print(data)

            elif command == "3":
                self.statistic()

class Record:
    def __init__(self):
        self.__courses = []

    def courses(self):
        return self.__courses
    
    def add_course(self, course):

        grade = course.grade

        found = None
        for crs in self.__courses:
            if crs.name() == course.name():
                found = crs
                if grade > crs.grade:
                    crs.grade = grade
        if found == None:
            self.__courses.append(course)

    def get_by_name(self, name):
        result = None
        for course in self.__courses:
            if course.name() == name:
                result = course
                break
        return result
    
    def statistic(self):
        total_credits = 0
        grade_total = 0
        five =0
        four = 0
        three = 0
        two = 0
        one = 0
        for course in self.__courses:
            total_credits+= course.credit()
            grade_total+= course.grade
            grade = course.grade
            if grade == 5:
                five+=1
            elif grade == 4:
                four+=1
            elif grade == 3:
                three+=1
            elif grade == 2:
                two+=1
            elif grade == 1:
                one+=1
        
        mean = grade_total/len(self.__courses)

        print(f"{len(self.__courses)} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        print(f"5: {'x' * five}")
        print(f"4: {'x' * four}")
        print(f"3: {'x' * three}")
        print(f"2: {'x' * two}")
        print(f"1: {'x' * one}")
        

class Course:
    def __init__(self, name, grade, credit):
        self.__name = name
        self.__grade = grade
        self.__credit = credit
    
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    def credit(self):
        return self.__credit
    
    def __str__(self):
        return f"{self.__name} ({self.__credit} cr) grade {self.__grade}"
    
app = Application()
app.execute()