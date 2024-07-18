# Write your solution here
examlist = []
examinput =[]
exerciselist = []
fail =0
summ = 0

def printstat():
    five =0
    four =0
    three =0
    two = 0
    one = 0
    zero =0
    # fail =0
    for i in examlist:
        if i>=0 and i<=14:
            zero+=1
            # fail+=1
        elif i>=15 and i<=17:
            one+=1
        elif i>=18 and i<=20:
            two+=1
        elif i>=21 and i<=23:
            three+=1
        elif i>=24 and i<=27:
            four+=1
        elif i>= 28 and i<=30:
            five+=1
    print("Statistics:")
    if len(examlist) > 0:
        print(f"Points average: {summ/len(examlist) :.1f}")
        print(f"Pass percentage: { (len(examlist)-fail)/len(examlist) *100:.1f}")
    else:
        print("Points average: 0.0")
        print("Pass percentage: 0.0")
    print("Grade distribution:")
    print(f"  5: {"*"*five}")
    print(f"  4: {"*"*four}")
    print(f"  3: {"*"*three}")
    print(f"  2: {"*"*two}")
    print(f"  1: {"*"*one}")
    print(f"  0: {"*"*zero}")
    # print("with the input:")
    # for i in range(len(exercise)):
    #     print(f"{examinput[i]} {exerciselist[i]}")

while True:
    numbers = input("Exam points and exercises completed: ")
    if numbers == "":
        printstat()
        break
    exam = int(numbers.split(" ")[0])
    exercise = int(numbers.split(" ")[1])
    summ+=exam
    examinput.append(exam)
    if exam < 10:
        fail+=1
    elif exam+ (exercise//10) <15:
        fail+=1
        
    exercise = int(numbers.split(" ")[1])
    summ+=exercise//10
    if exam >=10:
        exam+= exercise//10
    examlist.append(exam)
    exerciselist.append(exercise)
#18 80  15 60
#             words = "20 100;10 10;9 100;15 75;18 40;".split(";")         
#             expected = """Statistics:
# Points average: 20.8
# Pass percentage: 60.0
# Grade distribution:
#   5: *
#   4:
#   3: **
#   2:
#   1:
#   0: **""".split('\n')

#     def test_functionality_6(self):
#             words = "10 85;15 54;20 0;5 100;11 45;16 45;".split(";")         
#             expected = """Statistics:
# Points average: 18.0
# Pass percentage: 83.3
# Grade distribution:
#   5:
#   4:
#   3:
#   2: ****
#   1: *
#   0: *""".split('\n')


