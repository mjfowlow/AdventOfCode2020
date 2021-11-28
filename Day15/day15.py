#Day 15
print("--- Day 15: Rambunctious Recitation ---")

#                            ---- Problem 1 ----
#You catch the airport shuttle and try to book a new flight to your vacation island. 
#Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. 
#You take it.
#While you wait for your flight, you decide to check in with the Elves back at the North Pole. 
#They're playing a memory game and are ever so excited to explain the rules!
#In this game, the players take turns saying numbers. They begin by taking turns reading from a 
# list of starting numbers (your puzzle input). Then, each turn consists of considering the most recently spoken number:
#       -If that was the first time the number has been spoken, the current player says 0.
#       -Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
#        So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age (if the last number is a repeat).
#Their question for you is: what will be the 2020th number spoken? 

def problem1():
    #Input
    input = [1,0,18,10,19,6]

    #Keep track of positon
    position = 1
    
    #A list that creates dictionarys
    dictionary_list = []

    #For each number create a dictionary with the number as the key and the positon as the value
    for i in range(len(input) - 1):
        #Get next value in the input
        num = input[i]

        #Check if dictionary exists, if not the value will be "None"
        dict = next((dict for dict in dictionary_list if dict["number"] == num), None)
        
        #If dosen't exist creat new dictionary and it to the list
        if dict == None:
            new_dict = {
                "number" : num,
                "position" : position
            }
            dictionary_list.append(new_dict)
        
        #If it does exist update position and occurences
        else:
            #Update position and occurences
            dict["position"] = position
            #Get index of the dictionary and replace the old dictionary with the update one
            dict_index = next((i for i, dict in enumerate(dictionary_list) if dict["number"] == num), None)
            dictionary_list[dict_index] = dict
        
        #Increment position
        position += 1

    #Get last number 
    current_num = input[-1]
    #Keep track of the numbers spoken
    number_spoken = len(input) - 1

    while(number_spoken < 2020-1):
        #Check if dictionary exists, if not the value will be "None"
        dict = next((dict for dict in dictionary_list if dict["number"] == current_num), None)
    
        #If dosen't exist creat new dictionary
        if dict == None:
            new_dict = {
                "number" : current_num,
                "position" : position
            }
            dictionary_list.append(new_dict)
            #Update current number
            current_num = 0

        #If does exist, set current_num to difference of new positon and last position and update dict
        else:
            dict_index = next((i for i, dict in enumerate(dictionary_list) if dict["number"] == current_num), None)
            #set current num
            current_num = position - dict["position"]
            #Update dictionary
            dict["position"] = position
            #Add updated dictionary to the list
            dictionary_list[dict_index] = dict

        #Increment position and number_spoken    
        position += 1
        number_spoken += 1

    print("Problem 1 Output:", current_num)

problem1()


#                              ---- Problem 2 ----
#Impressed, the Elves issue you a challenge: determine the 30000000th number spoken.
#***Same problem as before but need to optimize solution as solution in problem 1 does not solve in a sufficent amount of time"
def problem2():
    input = [1,0,18,10,19,6]

    #Keep track of positon (Represents turn spoken)
    position = 1

    #Create a list where a index represents the number and the value at that index represents last time the number was spoken
    position_list = []

    #For each number in the input create a spot in the list
    for i in range(len(input) - 1):
        #Get number
        num = input[i]
        #If list don't have an index equal to num extend the list up to the length on num
        if(len(position_list)-1 < num):
            while(len(position_list) - 1 < num):
                #Add -1 to represent numbers that have a index but haven't been spoken yet
                position_list.append(-1)
            #Once have added all the values set the value to position
            position_list[num] = position
        #If list has a index for num set the value at index to position
        else:
             position_list[num] = position
        
        #Increment position
        position += 1


    #Get last number 
    current_num = input[-1]
    #Variable to keep track of number of turns 
    number_spoken = len(input) - 1

    while(number_spoken < 30000000-1):
        #Like before if the number dont have an index increment the list till it does
        if(len(position_list)-1 < current_num):
            while(len(position_list) - 1 < current_num):
                position_list.append(-1)

            #Update value at index and update current_num to 0 since it hasnt been spoken before
            position_list[current_num] = position
            current_num = 0
        #If list includes the index need to perform extra checks
        else:
            #If index exists but contains value of -1 it hasn't been spoken before
            #Set value to position and new current_num to 0
            if(position_list[current_num] == -1):
                position_list[current_num] = position
                current_num = 0
            #If do not have a value of -1, it has been spoken before so update position in list and calculate new current num
            else:
                #Calculate a temp value to hold what current_num will be since we will be changing value in the list
                new_num = position - position_list[current_num]
                position_list[current_num] = position 
                current_num = new_num

        #Increment position and number spoken
        position += 1
        number_spoken += 1

    print("Problem 2 Output:", current_num)


problem2()