#Day 4
print("--- Day 4: Passport Processing ---")

#                   ---- Problem 1 ----
#You arrive at the airport only to realize that you grabbed your North Pole
#Credentials instead of your passport. While these documents are extremely similar,
#North Pole Credentials aren't issued by a country and therefore aren't actually valid
#documentation for travel in most of the world.
#It seems like you're not the only one having problems, though; a very long line has formed
#for the automatic passport scanners, and the delay could upset your travel itinerary.
#Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
#The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields.
#The expected fields are as follows:
#       byr (Birth Year)
#       iyr (Issue Year)
#       eyr (Expiration Year)
#       hgt (Height)
#       hcl (Hair Color)
#       ecl (Eye Color)
#       pid (Passport ID)
#       cid (Country ID

#Count the number of valid passports - those that have all required fields. Treat cid as optional.
#In your batch file, how many passports are valid?

import re

def problem1():
    #Get input, split it blank lines
    passports = open("input.txt")
    passports = passports.read().split("\n\n")
    #After split you now have a list of strings
    #Need to split every string by a space or new line
    passports = [re.split('[" " | "\n"]', passport) for passport in passports]
    #Passports is now a 2 dimesional list

    #initiate number valid pasports and what a valid passport should look lie
    validPassports = 0
    validPassport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    #Iterate through the passports and add the code in the passport to a list
    for passport in passports:
        currentPassport = []
        for i in range(0, len(passport)):
            code = passport[i][:3:]
            currentPassport.append(code)
        #Check if currentPassport has all the elements of a valid passport    
        if(all(elem in currentPassport for elem in validPassport)):
            validPassports += 1
            
    print("Problem 1 Output:", validPassports)
        
problem1()

#                           ---- Problem 2 ----
#The line is moving more quickly now, but you overhear airport security talking
#about how passports with invalid data are getting through. Better add some data validation, quick!
#You can continue to ignore the cid field, but each other field has strict rules
#about what values are valid for automatic validation:

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.
#Your job is to count the passports where all required fields are both present and
#valid according to the above rules. Here are some example values:

#Count the number of valid passports - those that have all required fields and valid values.
#Continue to treat cid as optional. In your batch file, how many passports are valid?

def problem2():
    #Get input, split it blank lines
    passports = open("input.txt")
    passports = passports.read().split("\n\n")
    #After split you now have a list of strings
    #Need to split every string by a space or new line
    passports = [re.split('[" " | "\n"]', passport) for passport in passports]
    #Passports is now a 2 dimesional list

    #initiate number valid pasports and what a valid passport should look lie
    validPassports = []
    validPassport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    #Iterate through the passports and add the code in the passport to a list
    for passport in passports:
        currentPassport = []
        for i in range(0, len(passport)):
            code = passport[i][:3:]
            currentPassport.append(code)
        #Check if currentPassport has all the elements of a valid passport    
        if(all(elem in currentPassport for elem in validPassport)):
            validPassports.append(passport)

    #Now that eliminatyed all apssports that dont have right fields
    #Check that the passports values are correct
    
    eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid = 0
    
    for passport in validPassports:
        #sort codes alphabetically and remove cid code
        passport.sort()
        if(passport[1][:3:] == "cid"):
            passport.pop(1)
        
        #Get the code values
        byr = int(passport[0][4:len(passport[0]):])
        ecl = passport[1][4:len(passport[1]):]
        eyr = int(passport[2][4:len(passport[2]):])
        hcl = passport[3][4:len(passport[3]):]
        hgt = (passport[4][4:len(passport[4]):])
        iyr = int(passport[5][4:len(passport[5]):])
        pid = passport[6][4:len(passport[6]):]

        #Test byr
        if(byr < 1920 or byr > 2002):
            continue
        #Test ecl
        if(ecl not in eyeColors):
            continue
        #Test eyr
        if( eyr < 2020 or eyr > 2030):
            continue
        #Test hcl
        if(hcl[0] == "#" and len(hcl) == 7):
            hclFail = False
            for i in range(1, len(hcl)):
                if("a" > hcl[i] > "f" or "0" > hcl[i] > "9"):
                    hclFail = True
                    break
            if(hclFail):
                continue
        else:
            continue
        #Test hgt    
        if(hgt[len(hgt)-2:len(hgt):] == "in" or hgt[len(hgt)-2:len(hgt):] == "cm"):
            if(hgt[len(hgt)-2:len(hgt):] == "in"):
                if(int(hgt[:len(hgt)-2:]) < 59 or int(hgt[:len(hgt)-2:]) > 76):
                    continue
            else:
                if(int(hgt[:len(hgt)-2:]) < 150 or int(hgt[:len(hgt)-2:]) > 193):
                    continue
        else:
            continue
        #Test iyr
        if( iyr < 2010 or iyr > 2020):
            continue   
        #Test pid
        if(len(pid) != 9):
            continue
            
        #If made it here every test has passed so increment valid by 1
        valid += 1

    print("Problem 2 Output:",valid)
                        
                        
problem2()



