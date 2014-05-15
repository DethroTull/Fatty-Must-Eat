import random
import array

class Disaster:

    def __init__ (self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.tornado = ["tornado", random.randrange(0, self.max_x), random.randrange(0, self.max_y),
                   random.randrange(0, 5), random.randrange(0,3), random.randrange(1,11)]
        self.famine = ["famine", random.randrange(0,3), random.randrange(1,6)]
        self.flood = ["flood", random.randrange(0,3), random.randrange(1,4)]

    def genDisaster(self):
        d = random.randrange(0,3)

        if d == 0:
            print("\nSay good bye to your trailer and hello to FEMA!")
            print("A twister is upon us.")
            print("It will last for " + str(self.tornado[5]) + " days.")
            return self.tornado

        if d == 1:
            print("\nBird Flu! Mad Cow Disease! Feline Lukemia! The animals are all sick.")
            print("A famine is upon us.")
            print("It will last for " + str(self.famine[2]) + " days.")
            return self.famine

        else:
            print("\nRain rain go away. I have this stupid game to play.")
            print("A flood is upon us.")
            print("It will last for " + str(self.flood[2]) + " days.")
            return self.flood

    def getTornado(self):
        return self.tornado

    def getFamine(self):
        return self.famine

    def getFlood(self):
        return self.flood


    
