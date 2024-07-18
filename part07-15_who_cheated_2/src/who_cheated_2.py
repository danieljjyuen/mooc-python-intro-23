import csv
import datetime


def start_times():
    dict = {}
    with open("start_times.csv") as file_main:
        for lines in csv.reader(file_main, delimiter=";"):
            dict[lines[0]] = lines[1]
    return dict

def submissions():
    dict = {}
    start = start_times()
    with open("submissions.csv") as file_main:
        for lines in csv.reader(file_main, delimiter=";"):
           
            starttime = datetime.datetime.strptime(start[lines[0]], "%H:%M")
        
            subtime = datetime.datetime.strptime(lines[3], "%H:%M")

            if subtime < starttime + datetime.timedelta(hours=3):
                index = int(lines[1])
                if lines[0] not in dict:
                    dict[lines[0]] = [0,0,0,0,0,0,0,0]

                    dict[lines[0]][index-1] = int(lines[2])
                else:
                    if dict[lines[0]][index-1] < int(lines[2]):
                        dict[lines[0]][index-1] = int(lines[2])
    return dict

        
def final_points():
    sub = submissions()
    result = {}
    for student in sub:
        result[student] = sum(sub[student])
    return result
