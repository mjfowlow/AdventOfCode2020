#Day 11
print("--- Day 11: Seating System ---")

#                           ---- Problem 1 ----
#Your plane lands with plenty of time to spare. The final leg of your journey is
#a ferry that goes directly to the tropical island where you can finally start your
#vacation. As you reach the waiting area to board the ferry, you realize you're so early,
#nobody else has even arrived yet!
#By modeling the process people use to choose (or abandon) their seat in the waiting area,
#you're pretty sure you can predict the best place to sit. You make a quick map of the seat
#layout (your puzzle input).
#The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
#Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely
#predictable and always follow a simple set of rules. All decisions are based on the number of occupied
#seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal
#from the seat). The following rules are applied to every seat simultaneously:
#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#Otherwise, the seat's state does not change.
#Floor (.) never changes; seats don't move, and nobody sits on the floor.

#Simulate your seating area by applying the seating rules repeatedly until no seats change state.
#How many seats end up occupied?


def problem1():
    #Get seat Layout and split it up by row
    seatLayout = open("input.txt")
    seatLayout = seatLayout.read().split("\n")

    #Set the old seat layout to the intial seat Layout and calculate the new seat layour
    oldSeatLayout = seatLayout
    newSeatLayout = seatLayoutPattern(seatLayout)
    #While the seat layout keep changing keep updating it 
    while not oldSeatLayout == newSeatLayout:
        oldSeatLayout = newSeatLayout
        newSeatLayout = seatLayoutPattern(newSeatLayout)
    #Once we got the final seat layout count the number of occupied seats
    occupiedSeats = 0
    for row in range(0, len(newSeatLayout)):
        for col in range(0, len(newSeatLayout[0])):
            if newSeatLayout[row][col] == "#":
                occupiedSeats += 1
    print("Problem 1 Output:", occupiedSeats)
                
   
def seatLayoutPattern(seatLayout):
    #Break the new seat layout so rows are list and not strings.
    #This way they can be mutated
    newSeatLayout = [list(row) for row in seatLayout]

    numRows = len(seatLayout)
    numCols = len(seatLayout[0])

    #iterate through every seat 
    for row in range(0, numRows):
        for col in range(0, numCols):

            #if the location is not a seat but floor just continue
            if seatLayout[row][col] == ".":
                continue

            #count the number of occupied seats around the current seat
            occupiedSeats = 0
            for i in range(row-1, row+2):
                if i < 0 or i == numRows:
                        continue
                for j in range(col-1, col+2):
                    if j < 0 or j == numCols:
                            continue
                    if seatLayout[i][j] == "#":
                            occupiedSeats += 1

            #Make sure the current seat was not counted in the number of adjacent occupied seats
            #If number of occupied seats is greater then 4 set the seat to empty (L)
            if seatLayout[row][col] == "#":
                occupiedSeats-= 1
                if occupiedSeats >= 4:
                    newSeatLayout[row][col] = "L"
            #If the seat was empty and it had no adjacent occupied seats set it to occupied (#)
            if seatLayout[row][col] == "L" and occupiedSeats == 0:
                newSeatLayout[row][col] = "#"

    return newSeatLayout
                        
problem1()

#                                   ---- Problem 2 ----
#As soon as people start to arrive, you realize your mistake. People don't just care about
#adjacent seats - they care about the first seat they can see in each of those eight directions!
#Now, instead of considering just the eight immediately adjacent seats, consider the first seat
#in each of those eight directions.
#Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied
#seats for an occupied seat to become empty (rather than four or more from the previous rules). The
#other rules still apply: empty seats that see no occupied seats become occupied, seats matching no
#rule don't change, and floor never changes.

#Given the new visibility method and the rule change for occupied seats becoming empty, once
#equilibrium is reached, how many seats end up occupied?

def problem2():
    #Get seat Layout and split it up by row
    seatLayout = open("input.txt")
    seatLayout = seatLayout.read().split("\n")
    
    #Set the old seat layout to the intial seat Layout and calculate the new seat layour
    oldSeatLayout = seatLayout
    newSeatLayout = seatLayoutPattern2(seatLayout)
    #While the seat layout keep changing keep updating it 
    while not oldSeatLayout == newSeatLayout:
        oldSeatLayout = newSeatLayout
        newSeatLayout = seatLayoutPattern2(newSeatLayout)
    #Once we got the final seat layout count the number of occupied seats
    occupiedSeats = 0
    for row in range(0, len(newSeatLayout)):
        for col in range(0, len(newSeatLayout[0])):
            if newSeatLayout[row][col] == "#":
                occupiedSeats += 1
    print("Problem 2 Output:", occupiedSeats)

def seatLayoutPattern2(seatLayout):
    #Break the new seat layout so rows are list and not strings.
    #This way they can be mutated
    newSeatLayout = [list(row) for row in seatLayout]

    numRows = len(seatLayout)
    numCols = len(seatLayout[0])
    
    #Create a list of all pssible directions
    directions = ["up","right","down","left","up-right","down-right","down-left","up-left"]
     #iterate through every seat 
    for row in range(0, numRows):
        for col in range(0, numCols):

            #if the location is not a seat but floor just continue
            if seatLayout[row][col] == ".":
                continue

            #for each direction find the closest seat and increment occupiedseats accordingly 
            occupiedSeats = 0
            for direction in directions:
                occupiedSeats += nearestSeat(row, col, seatLayout, direction)

            #After calculating number of occupied seats update the seat values according to the rules
            if seatLayout[row][col] == "#" and occupiedSeats >= 5:
                newSeatLayout[row][col] = "L"
            if seatLayout[row][col] == "L" and occupiedSeats == 0:
                newSeatLayout[row][col] = "#"
    return newSeatLayout

def nearestSeat(row, col, seatLayout, direction):
    #While the nearest seat has not been found keep moving in the direction given
    nearestSeat = "."
    while nearestSeat == ".":
        if direction == "up":
            row -= 1
        if direction == "right":
            col += 1
        if direction == "down":
            row += 1
        if direction == "left":
            col -= 1
        if direction == "up-right":
            row -= 1
            col += 1
        if direction == "down-right":
            row += 1
            col += 1
        if direction == "down-left":
            row += 1
            col -= 1
        if direction == "up-left":
            row -= 1
            col -= 1
        #If the rw or cols go outside the boundarys of the seat layout break out of while loop
        if(row < 0 or row == len(seatLayout)):
            break
        if(col < 0 or col == len(seatLayout[0])):
            break
        #After each move update nearest seat
        nearestSeat = seatLayout[row][col]
    #If the nearest seat is occupied return 1 otherwise return 0
    if nearestSeat == "#":
        return 1
    else:
        return 0
            
problem2()
