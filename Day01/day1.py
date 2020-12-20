#Day1
print("--- Day 1: Report Repair ---")

#                   -----Problem 1-----  
#Before you leave, the Elves in accounting just need you to fix your
#expense report (your puzzle input);apparently, something isn't quite adding up.
#specifically, they need you to find the two entries that sum to 2020
#and then multiply those two numbers together.

#Find the two entries that sum to 2020; what do you get if you multiply them together?

def problem1():
    #Read file and add all numbers to a list
    expenseReport = open("input.txt")
    expenseReportNums = []
    for number in expenseReport:
        expenseReportNums.append(int(number))
    #Traverse list and check if any two values add to 2020
    for value in expenseReportNums:
        if(2020-value in expenseReportNums):
            answer1  = value * (2020-value)
            print("Problem 1 Output:", answer1)
            break

problem1()

#               -----Problem 2----- 
#The Elves in accounting are thankful for your help;
#one of them even offers you a starfish coin they had left over from a past vacation.
#They offer you a second one if you can find three numbers in your expense report
#that meet the same criteria.

#In your expense report, what is the product of the three entries that sum to 2020?

def problem2():
    #Read file and add all numbers to a list
    expenseReport = open("input.txt")
    expenseReportNums = []
    for number in expenseReport:
        expenseReportNums.append(int(number))
    #Set found to false
    found = False
    
    #Get an intial value
    for value1 in expenseReportNums:
        #If answer was found print and break
        if(found):
            break
        
        #Get a second value
        for value2 in expenseReportNums:
            #If value1 + value2 is greater then 2020 no need to check for third value
            if ((value1 + value2) < 2020):
                #Check if there any value that added with value1 and value2 equals 2020
                if (2020-(value1+value2) in expenseReportNums):
                    answer = value1 * value2 * (2020-(value1+value2))
                    print("Problem 2 Output:", answer)
                    found = True
                    break
            else:
                continue

problem2()
