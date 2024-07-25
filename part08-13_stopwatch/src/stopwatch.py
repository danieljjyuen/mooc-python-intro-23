# Write your solution here:
import datetime
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def __str__(self):
        min = self.minutes
        sec = self.seconds
        # if self.minutes < 10:
        #     min = "0"+str(min)
        # if self.seconds <10:
        #     sec = "0"+str(sec)
        # return f"{min}:{sec}"
        return datetime.time(minute=min, second=sec).strftime("%M:%S")

    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes <59:
                self.minutes+=1
            else:
                self.minutes =0
        else:
            self.seconds+=1


