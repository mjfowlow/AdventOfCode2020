#Day 10
print("--- Day 10: Adapter Array ---")

#                               ---- Problem 1 ----
#Patched into the aircraft's data port, you discover weather forecasts of a
#massive tropical storm. Before you can figure out whether it will impact your vacation plans,
#however, your device suddenly turns off! Its battery is dead.
#You'll need to plug it in. There's only one problem: the charging outlet near your seat produces
#the wrong number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.
#Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given
#adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
#In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated
#adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)
#Treat the charging outlet near your seat as having an effective joltage rating of 0.
#Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to
#your resort and realize you can't even charge your device!
#If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet,
#the adapters, and your device?
#Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count
#the joltage differences between the charging outlet, the adapters, and your device.

#What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

def problem1():
    #Get joltages change values from strings to ints
    joltages = open("input.txt")
    joltages = joltages.read().split("\n")
    joltages = [int(i) for i in joltages]
    
    #Intialize difference lists, joltage and find hightestJoltage
    difference1 = 0
    difference3 = 0
    joltage = 0
    highestJoltage = max(joltages) + 3
    while(True):
        #Check what adapted you have that connect to your current one
        #Start at 1 joltage increase to make sure you dont miss any adapters
        if(joltage + 1 in joltages):
            difference1 += 1
            joltage += 1
        elif(joltage + 2 in joltages):
            joltage += 2
        elif(joltage + 3 in joltages):
            difference3 += 1
            joltage += 3
        #If get to this point it means we are at the end of our list of adapters
        else:
            #Calculate if a 1 or 3 difference jump in joltage occurs
            if(joltage + 1 == highestJoltage):
                difference1 += 1
            elif(joltage + 3 == highestJoltage):
                difference3 += 1
            print("Problem 1 Output:",difference1*difference3)
            break

problem1()


#                                   ---- Problem 2 ----
#To completely determine whether you have enough adapters, you'll need to figure out how
#many different ways they can be arranged. Every arrangement needs to connect the charging
#outlet to your device. The previous rules about when adapters can successfully connect still apply.
#You glance back down at your bag and try to remember why you brought so many adapters; there must be
#more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

#What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

def problem2():
    #Get joltages change values from strings to ints
    joltages = open("input.txt")
    joltages = joltages.read().split("\n")
    joltages = [int(i) for i in joltages]
    #Add 0 to represent starting joltage and the max voltage +3 to reprsent ending voltage 
    joltages.extend([0, max(joltages) + 3])
    #Sort joltages
    joltages.sort()

    #Create a list of the size of joltages
    #Eacg location in the list represents how many combinations there are to get to that value
    combinations = [0 for i in range(len(joltages))]
    #Intialize first value to 1 as there only 1 combination to get the first value
    combinations[0] = 1
    #for each joltage update the different combinations to get to it by using the combinations possible before it
    for i in range(1, len(joltages)):
        for j in range(i-3,i):
            if joltages[i] - joltages[j] <= 3:
                combinations[i] += combinations[j]

    #Get possible combinations and print the value
    possibleCombinations = combinations[len(combinations)-1]
    print("Problem 2 Output:", possibleCombinations)
    
problem2()
