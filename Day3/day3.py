#Day 3
print("--- Day 3: Toboggan Trajectory ---")

#                               -----Problem 1-----                        
#You start on the open square (.) in the top-left corner and need to reach the bottom.
#The toboggan can only follow a few specific slopes (you opted for a cheaper model that
#prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
#From your starting position at the top-left, check the position that is right 3 and down 1.
#Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

#Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

def problem1():
    patterns = open("input.txt")
    patterns = patterns.read().split("\n")

    #Set x and treesHit to 0
    x = 0
    treesHit = 0
    #A tree is represented by #
    tree = "#"
    
    for pattern in patterns:
        if(pattern[x%len(pattern)] == tree):
            treesHit += 1
        x += 3
    print("Problem 1 output:",treesHit)

problem1()

#                              -----Problem 2----- 
#Determine the number of trees you would encounter if, for each of the following slopes,
#you start at the top-left corner and traverse the map all the way to the bottom:
#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.

#What do you get if you multiply together the number of trees encountered on each of the listed slopes?

def problem2():
    patterns = open("input.txt")
    patterns = patterns.read().split("\n")

    #Slopes = [right, down]
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    #Set treesHitTotal to 1 since you will be mutiplying 
    treesHitTotal = 1
    #A tree is represented by #
    tree = "#"
    for i in range(0, len(slopes)):
        x = 0
        index = 0
        treesHit = 0
        for pattern in patterns:
            #When dealing with 2 down skip every second pattern
            if(slopes[i][1] == 2):
                if(index % 2 == 1):
                    index += 1
                    continue;
                else:
                    index += 1
            #Test if location your at is a tree
            if(pattern[x%len(pattern)] == tree):
                treesHit += 1
            #Increment x by first value in slope
            x += slopes[i][0]
        treesHitTotal *= treesHit
    print("Problem 2 output:", treesHitTotal)

problem2()

