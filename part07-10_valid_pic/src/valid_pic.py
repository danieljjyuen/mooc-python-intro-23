import datetime
def is_it_valid(pic:str):
    if len(pic) != 11:
        return False
    control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    try:
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])

        marker = pic[6]
        if marker not in "+-A":
            return False

        markeryear = 0
        if marker == "+":
            markeryear = 1800
        elif marker =="-":
            markeryear = 1900
        elif marker == "A":
            markeryear = 2000
        
        markeryear +=yy
       
        datetime.datetime(markeryear, mm, dd)

        personalid = pic[7:10]
        controlchar = pic[10]

        if controlchar not in control:
            return False
        
        ninedigit = int(pic[0:6] + personalid)
    

        remainder = ninedigit%31
        if controlchar != control[remainder]:
            return False

        return True
    except ValueError:
        print("valueerror")
        return False
    
# print(is_it_valid("080842-720N"))