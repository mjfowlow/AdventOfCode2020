#Day 8
print("--- Day 8: Handheld Halting ---")

#                           ---- Problem 1 ----
#Your flight to the major airline hub reaches cruising altitude without incident.
#While you consider checking the in-flight menu for one of those drinks that come
#with a little umbrella, you are interrupted by the kid sitting next to you.
#Their handheld game console won't turn on! They ask if you can take a look.
#You narrow the problem down to a strange infinite loop in the boot code (your puzzle input)
#of the device. You should be able to fix it, but first you need to be able to run the code in isolation.
#The boot code is represented as a text file with one instruction per line of text. Each instruction
#consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

#-acc increases or decreases a single global value called the accumulator by the value given in the argument.
#The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
#-jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument
#as an offset from the jmp instruction. 
#-nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

#Run your copy of the boot code. Immediately before any instruction is executed a second time,
#what value is in the accumulator?

def problem1():
    #Get instruction
    instructions = open("input.txt")
    instructions = instructions.read().split("\n")


    accumulator = 0;
    index = 0
    instructionsCompleted = []
    while(True):
        #Check if instruction has been completed already
        if index in instructionsCompleted:
            break
        #Add the index to completed instructions     
        instructionsCompleted.append(index)
        #Get instruction and break up into operation and arguement
        instruction = instructions[index].split(" ")
        operation  = instruction[0]
        arguement = int(instruction[1])
        #If operation is acc change accumulator by arguement and increment index by 1 
        if(operation == "acc"):
            accumulator += arguement
            index += 1
        #If operation is jmp change index according to arguement
        elif(operation == "jmp"):
            index += arguement
        #If operation is nop increment index by 1
        else:
            index += 1
                
    print("Problem 1 Output", accumulator)

problem1()


#               ---- Problem 2 ----
#After some careful analysis, you believe that exactly one instruction is corrupted.
#Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed
#to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)
#The program is supposed to terminate by attempting to execute an instruction immediately
#after the last instruction in the file. By changing exactly one jmp or nop, you can repair
#the boot code and make it terminate correctly.

#Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
#What is the value of the accumulator after the program terminates?

def problem2():
    #Get instructions
    instructions = open("input.txt")
    instructions = instructions.read().split("\n")
    
    index = 0
    passed = False
    while(not passed):
        #Get operations and arguement
        instruction = instructions[index].split(" ")
        operation  = instruction[0]
        arguement = instruction[1]

        #If operation equals acc just increment index by one
        if(operation == "acc"):
            index += 1
        #Otherwise it is a jmp or nop so swap it
        else:
            if(operation == "jmp"):
                newInstructions = list(instructions)
                newInstructions[index] = ("nop " + arguement)
                #test if the new set of instructions pass
                passed = runInstructions(newInstructions)
            else:
                newInstructions = list(instructions)
                newInstructions[index] = ("jmp " + arguement)
                #Test if new set of instructions pass
                passed = runInstructions(newInstructions)
            index += 1
            

def runInstructions(instructions):
    
    accumulator = 0;
    index = 0
    instructionsCompleted = []
    while(True):
        #Check if instruction has been completed already
        if index in instructionsCompleted:
            return False
        #Add the index to completed instructions     
        instructionsCompleted.append(index)
        #Check if reached end of the list, if so print accumulator and return True        
        if index >= len(instructions):
            print("Problem 2 Output:", accumulator)
            return True
        #Get instruction and break up into operation and arguement
        instruction = instructions[index].split(" ")
        operation  = instruction[0]
        arguement = int(instruction[1])
        #If operation is acc change accumulator by arguement and increment index by 1 
        if(operation == "acc"):
            accumulator += arguement
            index += 1
        #If operation is jmp change index according to arguement
        elif(operation == "jmp"):
            index += arguement
        #If operation is nop
        else:
            index += 1
            
    
        

problem2()



