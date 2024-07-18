# Write your solution here
import datetime
import csv

def cheaters():
    #name;task;points; hh:mm
    submission = []
    with open("submissions.csv") as file_main:
        for line in csv.reader(file_main, delimiter=";"):
            if line == None:
                continue
            else:
                submission.append(line)
    start = {}
    with open("start_times.csv") as file_main:
        for line in csv.reader(file_main, delimiter=";"):
            if line == None:
                continue
            else:
                start[line[0]] = line[1]
    badlist = []
    for line in submission:
        name = line[0]
        parts = line[3].split(":")
        subhh = parts[0]
        submm = parts[1]
    
        startparts = start[name].split(":")
        #print(startparts)
        starthh = startparts[0]
        startmm = startparts[1]

        difference = datetime.timedelta(hours=int(subhh), minutes=int(submm)) - datetime.timedelta(hours=int(starthh), minutes=int(startmm))
        #print(difference)
        if datetime.timedelta(hours=3) < difference:
            #print(difference)
            badlist.append(name)
    return list(set(badlist))
#
#print(cheaters())