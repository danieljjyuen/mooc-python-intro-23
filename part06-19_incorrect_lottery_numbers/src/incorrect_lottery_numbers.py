# Write your solution here
#7 number


def filter_incorrect():
    with open("correct_numbers.csv","w") as file:
        pass
    with open("lottery_numbers.csv") as file_main:
        for lines in file_main:
            lines = lines.strip()
            
            try:
                parts = lines.split(";")
                week = parts[0].split(" ")
                weeknumber = int(week[1])

                listss = (parts[1].split(","))
                lists = list(map(int, listss))
                newset = list(set(lists))

                if len(lists) !=7 or len(newset)< len(lists):
                    raise ValueError
                
                for num in lists:
                    if num <1 or num >39:
                        raise ValueError
                
                add_entry(lines+"\n")
                
            except ValueError:
                print('invalid')

def add_entry(line):
    with open("correct_numbers.csv","a") as file_main:
        file_main.write(line)

#filter_incorrect()