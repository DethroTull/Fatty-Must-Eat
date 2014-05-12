import random
import array

class FMEmap:

    def __init__ (self, max_x, max_y, start_x, start_y, mp):
        self.max_x = max_x
        self.max_y = max_y
        self.hunt = [[random.randrange(0,4) for x in xrange(max_x)] for x in xrange(max_y)]
        self.plant = [[random.randrange(0,4) for x in xrange(max_x)] for x in xrange(max_y)]
        self.location = [start_x, start_y]
        self.mp = mp

    def displayHunt(self):
        cx = 0
        while cx < self.max_x:
            cy = 0
            while cy < self.max_y:
                print(str(self.hunt[cx][cy])),
                cy += 1
            print
            cx += 1

    def displayPlant(self):
        cx = 0
        while cx < self.max_x:
            cy = 0
            while cy < self.max_y:
                print(str(self.plant[cx][cy])),
                cy += 1
            print
            cx += 1

    def displayLocation(self):
        print(str(self.location[0]) + "," + str(self.location[1]))

    def getLocation(self):
        return self.location

    def moveMap(self):
        cm = 0
        while cm < self.mp:
            move = random.randrange(0,4)
            print("Move = " + str(move) + "\n")

            if move == 0:
                if self.location[0] > 0 and self.location[0] < self.max_x:
                    self.location[0] -= 1
                    print("Up 1\n")
                else:
                    print("Bump Top!")
            if move == 1:
                if self.location[1] > -1 and self.location[1] < (self.max_y - 1):
                    self.location[1] += 1
                    print("Right 1\n")
                else:
                    print("Bump Right!")
            if move == 2:
                if self.location[0] > -1 and self.location[0] < (self.max_x - 1):
                    self.location[0] += 1
                    print("Down 1\n")
                else:
                    print("Bump Bottom!")
            if move == 3:
                if self.location[1] > 0 and self.location[1] < self.max_y:
                    self.location[1] -= 1
                    print("Left 1\n")
                else:
                    print("Bump Left!")
            cm += 1
        cm = 0

    def getHunt(self):
        return self.hunt[self.location[0]][self.location[1]]

    def getPlant(self):
        return self.plant[self.location[0]][self.location[1]]
              

    
