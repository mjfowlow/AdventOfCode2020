#Day 6
print("--- Day 6: Custom Customs ---")

#                           ---- Problem 1 ----
#As your flight approaches the regional airport where you'll switch to a
#much larger plane, customs declaration forms are distributed to the passengers.
#The form asks a series of 26 yes-or-no questions marked a through z. All you need
#to do is identify the questions for which anyone in your group answers "yes". Since
#your group is just you, this doesn't take very long.
#However, the person sitting next to you seems to be experiencing a language barrier
#and asks if you can help. For each of the people in their group, you write down the
#questions for which they answer "yes", one per line.
#Another group asks for your help, then another, and eventually you've collected answers
#from every group on the plane (your puzzle input). Each group's answers are separated by
#a blank line, and within each group, each person's answers are on a single line.

#For each group, count the number of questions to which anyone answered "yes".
#What is the sum of those counts?


def problem1():
    #Get the inputs, split into group counts, and then each indiviual count
    counts = open("input.txt")
    counts = counts.read().split("\n\n")
    counts = [count.replace("\n", "") for count in counts]
    #Add each new question to a list
    sum = 0
    for count in counts:
        questions = []
        for i in range(len(count)):
            question = count[i]
            #If question is not already in list add it
            if question not in questions:
                questions.append(question)
        sum += len(questions)

    print("Problem 1 Output:", sum)

problem1()


#                           ---- Problem 2 ----
#As you finish the last group's customs declaration, you notice that you misread one word
#in the instructions: You don't need to identify the questions to which anyone answered "yes";
#you need to identify the questions to which everyone answered "yes"!

#For each group, count the number of questions to which everyone answered "yes".
#What is the sum of those counts?


def problem2():
    #Get the inputs, split into group counts, and then each indiviual count
    counts = open("input.txt")
    counts = counts.read().split("\n\n")
    counts = [count.split("\n") for count in counts]
    #Using sets calculate the intersection between each count 
    sum = 0
    for group in counts:
        #If the group is just one person at the total of their answers to sum
        if(len(group) == 1): 
            sum += len(group[0])
        else:
            #Set questions to the intial count in the group
            questions = set(group[0])
            #Iterate through every count taking the intersection 
            for i in range(1,len(group)):
                questions = questions.intersection(group[i])
                #If no intersection no point to keep checking
                if(len(questions) == 0):
                    break
            #The length of questions after iterating is how many questions were answered the same
            sum += len(questions)
    print("Problem 2 Output:",sum)
                                      
problem2()
