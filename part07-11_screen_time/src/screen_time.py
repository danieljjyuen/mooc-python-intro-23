# Write your solution here
import datetime
filename = input("Filename:")
startdate = input("Starting date:")
days = int(input("How many days:"))
sfdate = datetime.datetime.strptime(startdate, "%d.%m.%Y")
stringstartdate = sfdate.strftime("%d.%m.%Y")
endsfdate = sfdate+datetime.timedelta(days=days-1)
stringenddate = endsfdate.strftime("%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")
screentime = []
for i in range(days):
    date = datetime.datetime.strptime(startdate, "%d.%m.%Y")
    newdate = date+datetime.timedelta(days=i)
    ask = input(f"Screen time {newdate.strftime("%d.%m.%Y")}:")
    screentime.append(ask)

total = 0
format = []
for i in screentime:
    format.append(i.replace(" ", "/"))
    parts = i.split(" ")

    for p in parts:
        total+= int(p)

average = total/days


with open(filename, "w") as file_main:
    file_main.write(f"Time period: {stringstartdate}-{stringenddate}\n")
    file_main.write(f"Total minutes: {total}\n")
    file_main.write(f"Average minutes: {average}\n")

    for i in range(days):
        date = datetime.datetime.strptime(startdate, "%d.%m.%Y")
        newdate = date+datetime.timedelta(days=i)
        file_main.write(f"{newdate.strftime("%d.%m.%Y")}: {format[i]}\n")
        
print(f"Data stored in file {filename}")


