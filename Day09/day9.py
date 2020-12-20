#Day-9
print("--- Day 9: Encoding Error ---")

#                            ---- Problem 1 ----
#With your neighbor happily enjoying their video game, you turn your attention
#to an open data port on the little screen in the seat in front of you.
#Though the port is non-standard, you manage to connect it to your computer through
#the clever use of several paperclips. Upon connection, the port outputs a
#series of numbers (your puzzle input).
#The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which,
#conveniently for you, is an old cypher with an important weakness.
#XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive
#should be the sum of any two of the 25 immediately previous numbers. The two numbers will
#have different values, and there might be more than one such pair.
#as it is more than 25 numbers ago) was 20. Now, for the next number to be valid, there needs
#to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:

#The first step of attacking the weakness in the XMAS data is to find the first number in the
#list (after the preamble) which is not the sum of two of the 25 numbers before it.

#What is the first number that does not have this property?


def problem1():
    #Get numbers and change every value from string to int
    numbers = open("input.txt")
    numbers = numbers.read().split("\n")
    numbers = [int(i) for i in numbers]

    #Create Intial preambe and intialize index so it is one more then length of preamble
    preamble = [numbers[i] for i in range(25)]
    index = 25
    while(True):
        #Get number we are looking to find some fore
        value = numbers[index]
        foundSum = False
        for number in preamble:
            #Check if found sum and make sure sum is not number + number
            if(value - number in preamble and value-number != number):
                #If find sum add to new value to preambe and remove intial fist value
                preamble.append(numbers[index])
                preamble.pop(0)
                #Increment index and set foundSum to true
                index += 1
                foundSum = True
                break
        #If didn't find a sum print the value and break out of loop
        if not foundSum:
            print("Problem 1 Output:", value)
            break

problem1()

#                           ---- Problem 2 ----
#The final step in breaking the XMAS encryption relies on the invalid number you just
#found: you must find a contiguous set of at least two numbers in your list which sum
#to the invalid number from step 1.
#To find the encryption weakness, add together the smallest and largest number in this contiguous range;

#What is the encryption weakness in your XMAS-encrypted list of numbers?

def problem2():
    #Get numbers and change every value from string to int
    numbers = open("input.txt")
    numbers = numbers.read().split("\n")
    numbers = [int(i) for i in numbers]

    #Intialize index to 0 and set found to False to represent finding a set
    index = 0
    found = False
    while(not found):
        #Intialize sum to 0 and create a empty contigous set
        sumNumbers = 0
        contigousSet = []
        #Starting at index traverse through adding the values to sum
        for i in range(index,len(numbers)):
            value = numbers[i]
            #Check if our sum equals the target
            if sumNumbers + value == 104054607:
                contigousSet.append(value)
                maxNumber = max(contigousSet)
                minNumber = min(contigousSet)
                print("Problem 2 Output:", maxNumber+minNumber)
                found = True
                break
            #Else check if we can add the value to the sum and the set
            elif sumNumbers + value < 104054607:
                sumNumbers += value
                contigousSet.append(value)
            #If get here sum if greater then target so increase index and traverse again
            else:
                index += 1
                break
            
problem2()
