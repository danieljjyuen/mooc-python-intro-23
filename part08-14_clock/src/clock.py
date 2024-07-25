import datetime
# Write your solution here:
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return datetime.time(hour=self.hours, minute=self.minutes, second=self.seconds).strftime("%H:%M:%S")
    
    def tick(self):
        if self.seconds < 59:
            self.seconds+=1
        else:
            self.seconds =0
            if self.minutes <59:
                self.minutes+=1
            else:
                self.minutes = 0
                if self.hours <23:
                    self.hours+=1
                else:
                    self.hours=0
                    self.minutes=0
                    self.seconds =0
    def set(self, newhour, newminute):
        self.hours = newhour
        self.minutes = newminute
        self.seconds = 0
