# Write your solution here
# Remember the import statement
# from datetime import date


import datetime

def list_years(dates:list):
    result = []

    for date in dates:
        result.append(date.year)
    return sorted(result)
