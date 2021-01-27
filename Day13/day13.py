#Day 13
print("--- Day 13: Shuttle Search ---")

#                   ---- Problem 1 ----

def problem1():
    notes = open("input.txt")
    notes = notes.read().split("\n")
    notes[1] = notes[1].split(",")

    
    earliestTimeStamp = int(notes[0])
    #Earliest bus holds the Bus ID and the waiting time for that bus
    earliestBus = [100000, 100000]

    for bus in notes[1]:
        #Ignore buses out of service
        if bus == "x":
            continue
        else:
            #get the buses Time stamp
            timeStamp = int(bus)
            #Increment the timestamp by itself until greater then or equal to earliest time stamp
            while(timeStamp < earliestTimeStamp):
                timeStamp += int(bus)
            #Calculate waiting time
            waitingTime = timeStamp - earliestTimeStamp
            #If waiting time is less then the current earliest bus update it
            if waitingTime < earliestBus[1]:
                earliestBus[0] = int(bus)
                earliestBus[1] = waitingTime

    print("Problem 1 Output:",earliestBus[0] * earliestBus[1]) 

problem1()



