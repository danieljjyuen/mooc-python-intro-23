# Write your solution here
def printLayer(number) :
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = letters[0:number]
    letters = letters[::-1]
    side = (number*2)-1
    matrix =[]

    for i in range(side):
        matrix.append([])
        for j in range(side):
            matrix[i].append("")
    
    count =0
    for i in letters:
        for x in range(0+count, side-count):
            for y in range (0+count, side-count):
                matrix[x][y] = i
        count+=1
    
    for x in range(side):
        line = ""
        for y in range(side):
            line+= matrix[x][y]
        print(line)

ask = int(input("Layers:"))

printLayer(ask)
    
    
