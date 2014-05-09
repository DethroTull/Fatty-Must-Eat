import random

class Fatty:

    def __init__ (self):
        print("A wild Fatty appears!")
        self.int = random.randrange(0,3)
        self.max_hunger = 10
        self.hunger = 10
        self.foraging = random.randrange(0,3)
        self.max_hp = 5
        self.hp = 5
        self.max_ap = random.randrange(2,5)
        self.dead = 0
        self.hunting = random.randrange(0,3)
