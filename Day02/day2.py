#Day 2
print("--- Day 2: Password Philosophy ---")

#                               -----Problem 1----- 
#The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
#"Something's wrong with our computers; we can't log in!" You ask if you can take a look.
#Their password database seems to be a little corrupted:
#some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy
#that was in effect when they were chosen.
#
#Each line gives the password policy and then the password.
#The password policy indicates the lowest and highest number of times a given letter
#must appear for the password to be valid. For example, 1-3 a means that the password must
#contain a at least 1 time and at most 3 times.
#How many passwords are valid according to their policies?

import re

def problem1():
    valid = 0
    passwords = open("input.txt")
    #Iterate through every policy and pasowrd
    for values in passwords:
        #split line to get range, character, and password

        values = re.split('[-|:|" "| \n]', values)
        lowerBound = int(values[0])
        upperBound = int(values[1])
        character = values[2]
        password = values[4]
    
        #Calculate how many times character is seen in the password
        characterTotal = 0
        for i in range(0, len(password)):
            if(character == password[i]):
                characterTotal += 1
        #chekc if passwod is valid or not
        if (lowerBound <= characterTotal <= upperBound):
            valid += 1
    print("Problem 1 output:", valid)
        
 
problem1()

#                       -----Problem 2----- 
#The shopkeeper suddenly realizes that he just accidentally explained the
#password policy rules from his old job at the sled rental place down the street!
#The Official Toboggan Corporate Policy actually works a little differently.
#Each policy actually describes two positions in the password, where 1 means the first
#character, 2 means the second character, and so on.
#Exactly one of these positions must contain the given letter.

#How many passwords are valid according to the new interpretation of the policies?

def problem2():
    valid = 0
    passwords = open("input.txt")
    #Iterate through every policy and pasowrd
    for values in passwords:
        #split line to get positions, character, and password
        values = re.split('[-|:|" "| \n]', values)
        position1 = (int(values[0])) - 1
        position2 = (int(values[1])) - 1
        character = values[2]
        password = values[4]
        #Check if either position contains the character
        if(password[position1] == character or password[position2] == character):
            #Make sure both do not contain the character
            if(password[position1] == character and password[position2] == character):
                continue
            else:
                valid += 1
    print("Problem 2 output:", valid)

problem2()
    
