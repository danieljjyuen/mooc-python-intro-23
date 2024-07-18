# Write your solution here

import datetime
day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
cal = datetime.datetime(year, month, day)
eve = datetime.datetime(1999,12,31)
diff = eve - cal
if year >= 2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {diff.days} days old on the eve of the new millennium.")
