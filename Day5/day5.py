#Day 5
print("--- Day 5: Binary Boarding ---")

#                           ---- Problem 1 ----
#You board your plane only to discover a new problem: you dropped your boarding pass!
#You aren't sure which seat is yours, and all of the flight attendants are busy with
#the flood of people that suddenly made it through passport control.
#The first 7 characters will either be F or B; these specify exactly one of the 128 rows
#on the plane (numbered 0 through 127). Each letter tells you which half of a region the
#given seat is in. Start with the whole list of rows; the first letter indicates whether
#the seat is in the front (0 through 63) or the back (64 through 127). The next letter
#indicates which half of that region the seat is in, and so on until you're left with exactly one row
#Every seat also has a unique seat ID: multiply the row by 8, then add the column. 

#As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

def problem1():
    #Get boarding passes and split by pass
    boardingPasses = open("input.txt")
    boardingPasses = boardingPasses.read().split("\n")

    #Iterate through every pass, get row, column, seat id, and max seat id
    maxSeatId = 0
    for boardingPass in boardingPasses:
        #Get row
        lowerRow = 0
        upperRow = 127
        for i in range(0, 7):
            difference = upperRow - lowerRow
            if(boardingPass[i] == "F"):
                upperRow = lowerRow +(difference // 2)
            else:
                lowerRow = upperRow -(difference // 2)
            row = upperRow
        #Get Column
        lowerColumn = 0
        upperColumn = 7
        for i in range(7, 10):
            difference = upperColumn - lowerColumn
            if(boardingPass[i] == "L"):
                upperColumn = lowerColumn +(difference // 2)
            else:
                lowerColumn = upperColumn -(difference // 2)
            column = upperColumn
	#calculate seatID
        seatId = row * 8 + column
        if(seatId > maxSeatId):
            maxSeatId = seatId
    print("Problem 1 Output:", maxSeatId)
    

problem1()


#                           ---- Problem 2 ----
#Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#It's a completely full flight, so your seat should be the only missing boarding pass
#in your list. However, there's a catch: some of the seats at the very front and back
#of the plane don't exist on this aircraft, so they'll be missing from your list as well.
#Your seat wasn't at the very front or back, though;
#the seats with IDs +1 and -1 from yours will be in your list.

#What is the ID of your seat?

    
