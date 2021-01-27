#Day 14
print("--- Day 14: Docking Data ---")

#               ---- Problem 1 ----


def problem1():
    program = open("test.txt")
    program = program.read().split("\n")

    mask = program[0][7:len(program[0])]
    memory = [0] * 67108863

    for line in program:

        if line[0:4] == "mask":
            mask = line[7:len(line)]
            print("Mask:",mask)

        if line[0:3] == "mem":
            address = line[line.find("[")+1:line.find("]")]
            value = int(line[line.find("=")+2:len(line)])
            value = f'{value:036b}'
            print("Valu:",value)
            for i in range(0,len(mask)):
                result = []
                print("m:", mask[i], " v:",value[i]) 
                if mask[i] == "1" or mask[i] == "0":
                    result.append(int(mask[i]))
                if mask[i] == "X":
                    result.append(value[i])

    
problem1()
