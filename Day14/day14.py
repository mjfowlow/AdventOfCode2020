#Day 14
print("--- Day 14: Docking Data ---")

#                                       ---- Problem 1 ----
# As your ferry approaches the sea port, the captain asks for your help again. The computer system 
# that runs this port isn't compatible with the docking program on the ferry, so the docking parameters 
# aren't being correctly initialized in the docking program's memory. After a brief inspection, you discover 
# that the sea port's computer system uses a strange bitmask system in its initialization program. Although 
# you don't have the correct decoder chip handy, you can emulate it in software!
# The initialization program (your puzzle input) can either update the bitmask or write a value to memory.
# Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, 
# a line like mem[8] = 11 would write the value 11 to memory address 8.
# The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35)
# on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is 
# applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in 
# the value, while an X leaves the bit in the value unchanged. Execute the initialization program. 
# What is the sum of all values left in memory after it completes? 

def problem1():
    #Read input data
    program = open("input.txt")
    program = program.read().split("\n")

    #Intialize memory to all 0
    memory = [0] *  67108863
 
    #Iterate through every line of the input
    for line in program:
        #If line begin with mask update mask value
        if line[0:4] == "mask":
            mask = line[7:len(line)]
        #If line begins with mem get memory address and value to add 
        if line[0:3] == "mem":
            address = int(line[line.find("[")+1:line.find("]")])
            value = int(line[line.find("=")+2:len(line)])
            #Set value to 36 bit binary value
            value = f'{value:036b}'
            
            #Compare mask and value
            result = ""
            for i in range(0,len(mask)): 
                if mask[i] == "1" or mask[i] == "0":
                    result += mask[i]
                if mask[i] == "X":
                    result += value[i]
            #Convert binary string to an integer and add to memory
            memory[address] = int(result,2)
    #Ater iterating throuhg input sum values in memory
    memorySum = sum(memory)
    #Print answer
    print("Problem 1 Output:",memorySum)

problem1()


#                                       ---- Problem 2 ----
# For some reason, the sea port's computer system still can't communicate with your ferry's docking program. 
# It must be using version 2 of the decoder chip! A version 2 decoder chip doesn't modify the values being 
# written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to 
# memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the 
# following way:
#               - If the bitmask bit is 0, the corresponding memory address bit is unchanged.
#               - If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
#               - If the bitmask bit is X, the corresponding memory address bit is floating.
# A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means 
# the floating bits will take on all possible values, potentially causing many memory addresses to be written 
# all at once!
# Execute the initialization program using an emulator for a version 2 decoder chip. 
# What is the sum of all values left in memory after it completes?

def problem2():
    #Read input data
    program = open("input.txt")
    program = program.read().split("\n")

    #Intialize memory
    memory = []
 
    #Iterate through every line of the input
    for line in program:
        #If line begin with mask update mask value
        if line[0:4] == "mask":
            mask = line[7:len(line)]
        #If line begins with mem get memory address and value to add 
        if line[0:3] == "mem":
            address = int(line[line.find("[")+1:line.find("]")])
            value = int(line[line.find("=")+2:len(line)])
            #Set address to 36 bit binary value
            address = f'{address:036b}'
            
            # Compare mask and value
            # Intialize result as a string, numberX as the number of x's in our result and 
            # positionX represents where the x's are located in our result
            result = ""
            numberX = 0
            positionX = []
            for i in range(0,len(mask)): 
                if mask[i] == "1":
                    result += mask[i]
                if mask[i] == "0":
                    result += address[i]
                if mask[i] == "X":
                    result += "X"
                    numberX += 1
                    positionX.append(i)

            #Create a list of binary strings the size of the number of x's in result 
            permutations = [bin(x)[2:].rjust(numberX, '0') for x in range(2**numberX)] 
            
            #Change result to a list so we can modify its x's
            result = list(result)
            results = []
            #For each permuation we will adjust our x values according to the permutation
            for permuation in permutations:
                for i in range(len(permuation)):
                    result[positionX[i]] = permuation[i]
                #When we add the results to the list results we convert it back to a string
                results.append(int("".join(result),2))
            #for each result (or address we should say) we add the value 
            for address in results:
                #Guidance for finding dictionary from
                #https://stackoverflow.com/questions/3897499/check-if-value-already-exists-within-list-of-dictionaries
                #Look to see if address exists, if not add address and value
                if not any(d['address'] == address for d in memory):
                    newAddress = {"address": address, "value": value}
                    memory.append(newAddress)
                #otherwise find dict and update it  
                else:
                    d = next(item for item in memory if item['address'] == address)
                    d['value'] = value


    #After adding all values to memory sum the list and print it
    memorySum = sum(item['value'] for item in memory)
    print("Problem 2 Output:",memorySum)

problem2()


