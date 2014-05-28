#MapClass for FME
#This class requires a maximum x and y to generate the maps
#self.hunt will randomly generate the hunting food values between 0 and 3
#self.plant will randomly generate the foraging food values between 0 and 3
#displayHunt will print out the current values for the hunting map
#displayPlant will print out the current values for the foraging map
#moveMap takes in a location array and movement points to calculate the random
#   movement and returns the new locatoin array
#getHunt takes in a location array and returns the current food value
#getPlant takes in a location array and returns the current food value

import random
import array

class FMEmap:

    gridMap = []

    #Class constructor for hunting and foraging map generation
    def __init__ (self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.hunt = [[random.randrange(0,4) for x in xrange(max_x)] for x in xrange(max_y)]
        self.plant = [[random.randrange(0,4) for x in xrange(max_x)] for x in xrange(max_y)]
        self.gridMap = [[0 for j in range(max_x)] for i in range(max_y)] 

        self.initGrid()


    def initGrid(self):
        i = 0
        for i in range(self.max_x):
            j = 0
            for j in range(self.max_y):
                self.gridMap[i][j] = []

    #function for printing out the current hunting food values
    def displayHunt(self):
        cx = 0
        print("Hunts")
        while cx < self.max_x:
            cy = 0
            while cy < self.max_y:
                print(str(self.hunt[cx][cy])),
                cy += 1
            print
            cx += 1

    #function for printing out the current foraging food values
    def displayPlant(self):
        print("Plants")
        cx = 0
        while cx < self.max_x:
            cy = 0
            while cy < self.max_y:
                print(str(self.plant[cx][cy])),
                cy += 1
            print
            cx += 1

    #function for random movement on the map
    def moveMap(self, location, mp):
        cm = 0
        while cm < mp:
            move = random.randrange(0,4) #generate a random number for direction
            #print("Move = " + str(move) + "\n")

            #calculate the new location based on the move RNG result
            #if the random move is off the grid the location is left as the same
            #   and the mp is lost
            if move == 0:
                if location[0] > 0 and location[0] < self.max_x:
                    location[0] -= 1
                   # print("Up 1\n")
                #else:
                    #print("Bump Top!\n")
            if move == 1:
                if location[1] > -1 and location[1] < (self.max_y - 1):
                    location[1] += 1
                    #print("Right 1\n")
                #else:
                    #print("Bump Right!\n")
            if move == 2:
                if location[0] > -1 and location[0] < (self.max_x - 1):
                    location[0] += 1
                    #print("Down 1\n")
                #else:
                    #print("Bump Bottom!\n")
            if move == 3:
                if location[1] > 0 and location[1] < self.max_y:
                    location[1] -= 1
                    #print("Left 1\n")
                #else:
                    #print("Bump Left!\n")
            cm += 1
        cm = 0
        return location #return the new location array

    def moveEntity(self, entity):
        oldlocation = [entity.location[0], entity.location[1]]
        newLocation = self.moveMap(entity.location, entity.mp)

        if self.gridMap[oldlocation[0]][oldlocation[1]].count(entity) > 0:
            index = self.gridMap[oldlocation[0]][oldlocation[1]].index(entity) 
            self.gridMap[oldlocation[0]][oldlocation[1]].remove(entity)

        self.gridMap[newLocation[0]][newLocation[1]].append(entity)
        print entity.fullname + " moved from " + str(oldlocation) + " to " + str(entity.location)

    def displayGrid(self):
        for row in self.gridMap:
            print row
        pass


    #function to return the current hunting value if it is between 1 and 3
    #If the value is returned the new value is set to 9
    #If the value is 9 or 0 the function returns a 0
    def getHunt(self, location):
        if self.hunt[location[0]][location[1]] > 0 and self.hunt[location[0]][location[1]] != 9:
            food = self.hunt[location[0]][location[1]]
            self.hunt[location[0]][location[1]] = 9
            return food
        else:
            return 0

    #function to return the current foraging value if it is between 1 and 3
    #If the value is returned the new value is set to 9
    #If the value is 9 or 0 the function returns a 0
    def getPlant(self, location):
        if self.plant[location[0]][location[1]] > 0 and self.plant[location[0]][location[1]] != 9:
            food = self.plant[location[0]][location[1]]
            self.plant[location[0]][location[1]] = 9
            return food
        else:
            return 0
              

    
