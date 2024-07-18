import string

def run(program):
    variables = {}
    result = []
    location = {}
    for i in range(len(program)):
        if ":" in program[i]:
            location[program[i][:-1]] = i
    for letter in string.ascii_uppercase:
        variables[letter] = 0
    index =0
    while index < len(program):
        command = program[index]
        if command == "END":
            return result
        elif "PRINT " in command:
            parts = command.split(" ")
            if parts[1] in string.ascii_uppercase:
                result.append(variables[parts[1]])
            else:
                result.append(int(parts[1]))
        elif "MOV " in command:
            parts = command.split(" ")
            if parts[2] in string.ascii_uppercase:
                variables[parts[1]] = int(variables[parts[2]])
            else:
                variables[parts[1]] = int(parts[2])
        elif "ADD " in command:
            parts = command.split(" ")
            if parts[2] in string.ascii_uppercase:
                variables[parts[1]] += int(variables[parts[2]])
            else:
                variables[parts[1]] += int(parts[2])
        elif "SUB " in command:
            parts = command.split(" ")
            if parts[2] in string.ascii_uppercase:
                variables[parts[1]] -= int(variables[parts[2]])
            else:
                variables[parts[1]] -= int(parts[2])
        elif "MUL " in command:
            parts = command.split(" ")
            if parts[2] in string.ascii_uppercase:
                variables[parts[1]] *= int(variables[parts[2]])
            else:
                variables[parts[1]] *= int(parts[2])
        elif "IF " in command and "JUMP" in command:
            parts = command.split(" ")
            
            evaluate = "".join(parts[1: parts.index("JUMP")])
            var1 = evaluate[0]
            var2 = evaluate[-1]
            if var1 in string.ascii_uppercase:
                var1 = int(variables[var1])
        
                
            if var2 in string.ascii_uppercase:
                var2 = int(variables[var2])

            if eval(str(var1) + evaluate[1:-1] + str(var2)):
                index = int(location[parts[-1]])
        elif "JUMP " in command:
            parts = command.split(" ")
            index = int(location[parts[1]+":"])
        
        else:
            location[command] = index
        index+=1
    
    return result

#run(['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start'])