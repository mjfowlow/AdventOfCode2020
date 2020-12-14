#Day 7
print("--- Day 7: Handy Haversacks ---")

#                   --- Problem 1 ---
#You land at the regional airport in time for your next flight. In fact,
#it looks like you'll even have time to grab some food: all flights are
#currently delayed due to issues in luggage processing.
#Due to recent aviation regulations, many rules (your puzzle input) are being
#enforced about bags and their contents; bags must be color-coded and must contain
#specific quantities of other color-coded bags. Apparently, nobody responsible for
#these regulations considered how long they would take to enforce!
#You have a shiny gold bag. If you wanted to carry it in at least one other bag, how
#many different bag colors would be valid for the outermost bag? (In other words: how
#many colors can, eventually, contain at least one shiny gold bag?)

#How many bag colors can eventually contain at least one shiny gold bag?

def problem1():
    #get regulations
    regulations = open("input.txt")
    regulations = regulations.read().split("\n")

    outerBags = ["shiny gold"]
    orgLength = 0
    newLength = -1
    #Loop till find no new outer bags
    while(orgLength != newLength):
        orgLength = len(outerBags)
        outerBags = findOuterBags(regulations, outerBags)
        newLength = len(outerBags)
    print("Problem 1 Output:",len(outerBags) - 1)
    
    
def findOuterBags(regulations, outerBags):
    newOuterBags = []
    for regulation in regulations:
        for bag in outerBags:
            if bag in regulation:
                split = regulation.split(" ")
                outerBag = split[0] + " " + split[1]
                if outerBag in outerBags or outerBag in newOuterBags:
                    continue
                else:
                    newOuterBags.append(outerBag)
    return outerBags + newOuterBags
    
problem1()

#                       ---- Problem 2 ----
#It's getting pretty expensive to fly these days - not because of ticket prices,
#but because of the ridiculous number of bags you need to buy!

#How many individual bags are required inside your single shiny gold bag?

def problem2():
    #get regulations
    regulations = open("input.txt")
    regulations = regulations.read().split("\n")
    regulations  = [regulation.split(" ") for regulation in regulations]
    #Get the contents of shiny bag
    shinyGoldBag = []
    for regulation in regulations:
        #Chech if the regulation is the shiny gold bag regulation
        if (regulation[0] + " " + regulation[1]) == "shiny gold":
            bagsTotal = 0
            for i in range(4,len(regulation),4):
                bagsTotal += int(regulation[i]) 
                bagList = []
                bagList.append(int(regulation[i]))
                bagList.append(regulation[i+1] + " " + regulation[i+2])
                shinyGoldBag.append(bagList)
    
    #Here is where we search for the contents in shinyBag
    newBags = shinyGoldBag
    while(len(newBags) != 0):
        newBags2= []
        for regulation in regulations:
            for bag in newBags:
                #Searching for the name of bag regulation
                nameBag = bag[1]
                regulationName = regulation[0] + " " + regulation[1]
                if nameBag == regulationName:
                   for i in range(4,len(regulation),4):
                       newBag = []
                       #If bag contians no other bags continue
                       if(regulation[i] == "no"):
                           break
                       #Get how many bags and name of this color
                       newBag.append(int(regulation[i]) * bag[0])
                       newBag.append(regulation[i+1] + " " + regulation[i+2])
                       newBags2.append(newBag)
                       #Add new amount of bags to bagTotal
                       bagsTotal += newBag[0]
        newBags = newBags2
    print("Problem 2 Output:", bagsTotal)

problem2()
            
