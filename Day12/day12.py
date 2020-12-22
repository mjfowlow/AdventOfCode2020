#Day 12
print("--- Day 12: Rain Risk ---")

#                           ---- Problem 1 ----
#Your ferry made decent progress toward the island, but the storm came in
#faster than anyone expected. The ferry needs to take evasive actions!
#Unfortunately, the ship's navigation computer seems to be malfunctioning; rather
#than giving a route directly to safety, it produced extremely circuitous instructions.
#When the captain uses the PA system to ask if anyone can help, you quickly volunteer.
#The navigation instructions (your puzzle input) consists of a sequence of single-character
#actions paired with integer input values. After staring at them for a few minutes, you work
#out what they probably mean:

#Action N means to move north by the given value.
#Action S means to move south by the given value.
#Action E means to move east by the given value.
#Action W means to move west by the given value.
#Action L means to turn left the given number of degrees.
#Action R means to turn right the given number of degrees.
#Action F means to move forward by the given value in the direction the ship is currently facing.

#The ship starts by facing east. Only the L and R actions change the direction the ship is facing.
#(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10
#units, but would still move east if the following action were F.)

#Figure out where the navigation instructions lead.
#What is the Manhattan distance between that location and the ship's starting position?

def problem1():
    #Get instructions and break into individual instructions
    instructions = open("input.txt")
    instructions = instructions.read().split("\n")

    #Intialize directionFacing, horDistance, verDistance, direction list
    directionFacing = "E"
    horDistance = 0
    verDistance = 0
    directions = ["E", "S", "W", "N"]

    
    for instruction in instructions:
        #For each instruction get the direction and magnitude
        direction = instruction[0]
        magnitude = int(instruction[1:len(instruction)])

        #If direction is F need to move forward in our directionFacing
        if direction == "F":
            if directionFacing == "E":
                horDistance += magnitude
            elif directionFacing == "W":
                horDistance -= magnitude
            elif directionFacing == "N":
                verDistance += magnitude
            else:
                verDistance -= magnitude

        #Given direction [N,S,E,W] increment distance accordingly 
        elif direction == "N":
            verDistance += magnitude
        elif direction == "S":
            verDistance -= magnitude
        elif direction == "E":
            horDistance += magnitude
        elif direction == "W":
            horDistance -= magnitude

        #If not given F or direction need to rotate
        else:
            #Get locaiton of direction facing in direction list
            index = directions.index(directionFacing)
            #Get amount of degrees to turn 
            degrees = magnitude//90
            #If direction to turn is right (R) add the amount od degees
            if direction == "R":
                directionFacing = directions[(index+degrees)%4]
            #Otherwise need to turn left so subtract degrees
            else:
                directionFacing = directions[index-degrees]

    print("Problem 1 Output",abs(horDistance) + abs(verDistance))
    
problem1()


#                            ---- Problem 2 ----
#Before you can give the destination to the captain, you realize that the actual action
#meanings were printed on the back of the instructions the whole time.
#Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

#Action N means to move the waypoint north by the given value.
#Action S means to move the waypoint south by the given value.
#Action E means to move the waypoint east by the given value.
#Action W means to move the waypoint west by the given value.
#Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
#Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
#Action F means to move forward to the waypoint a number of times equal to the given value.

#The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship;
#that is, if the ship moves, the waypoint moves with it.

#Figure out where the navigation instructions actually lead.
#What is the Manhattan distance between that location and the ship's starting position?

def problem2():
    #Get instructions and break into individual instructions
    instructions = open("input.txt")
    instructions = instructions.read().split("\n")
    
    #Intialize way point, horziontal disctance, and vertical distance
    wayPoint = [10, 1]
    horDistance = 0
    verDistance = 0
    for instruction in instructions:
        #For each instruction get the direction and magnitude
        direction = instruction[0]
        magnitude = int(instruction[1:len(instruction)])

        #If direction is F need to move forward in our directionFacing
        if direction == "F":
            horDistance += magnitude * wayPoint[0]
            verDistance += magnitude * wayPoint[1]

        #If direction is [N,S,E,W] increment waypoint accordingly
        elif direction == "N":
            wayPoint[1] += magnitude
        elif direction == "S":
            wayPoint[1] -= magnitude
        elif direction == "E":
            wayPoint[0] += magnitude
        elif direction == "W":
            wayPoint[0] -= magnitude

        #If not given F or direction need to rotate
        else:
            #if magnitude is 180 does not matter if rotation is left or right
            #Swap values and take the inverse of both
            if magnitude == 180:
                    wayPoint[0] = -wayPoint[0]
                    wayPoint[1] = -wayPoint[1]
            if direction == "R":
                if magnitude == 90:
                    temp = wayPoint[0]
                    wayPoint[0] = wayPoint[1]
                    wayPoint[1] = -temp
                elif magnitude == 270:
                    temp = wayPoint[0]
                    wayPoint[0] = -wayPoint[1]
                    wayPoint[1] = temp
            elif direction == "L":
                if magnitude == 90:
                    temp = wayPoint[0]
                    wayPoint[0] = -wayPoint[1]
                    wayPoint[1] = temp
                elif magnitude == 270:
                    temp = wayPoint[0]
                    wayPoint[0] = wayPoint[1]
                    wayPoint[1] = -temp

    print("Problem 2 Output",abs(horDistance) + abs(verDistance))
            

    
problem2()
