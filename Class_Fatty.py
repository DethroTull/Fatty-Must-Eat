import random

class Fatty:
    """ This is the main Fatty class """
    sayings = ['Butter!  Fatty want butter!',
               'Feeeed mmmmeeeeeee!',
               'Dis look tasty to fatty!'] 

    def __init__(self):
        print("A wild Fatty appears!")

    def talk(self):
        should_talk = random.randrange(0,5)

        if should_talk == 3:
            fatty_saying = random.randrange(0, len(self.sayings))
            print("\nFatty sez: " + self.sayings[fatty_saying] + "\n")
        
