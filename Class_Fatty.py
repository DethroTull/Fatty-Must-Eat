import random

class Fatty:
    """ This is the main Fatty class """
    sayings = ['Butter!  Fatty want butter!',
               'Feeeed mmmmeeeeeee!',
               'Dis look tasty to fatty!',
               'Fatty want more food.',
               'Crisco on everything.',
               'Do you like ranch?',
               'Diet coke has 1 calorie.',
               'I might have diabetes.',
               'It\'s a glandular problem.',
               'This pizza needs more ranch.']
    names = {'man' : ['Ronald', 'Donald', 'Bert', 'Jim', 'Shawn', 'Alex', 'Paulie', 'Bill', 'Owen'],
             'woman' : ['Bertha', 'Rosie', 'Trudy', 'Edith', 'Edna', 'Helga', 'Olga', 'Denise', 'Shelby', 'Kristie', 'Shawna', 'La Keisha', 'Cinnamon', 'Joannie'],
             'last' : ['McButterpants', 'Heffer', 'The Huge', 'Porcine', 'Rolls', 'O\'Crisco', 'Tubs', 'McFats', 'Von Rolls', 'El Chub']
            }
    sexes = ['man', 'woman']
    deaths = ['died of diabetes.',
            'died of a heart attack.',
            'choked on a bone and died.',
            'died of gallbladder cancer.',
            'stroked out and died.',
            'died of fatty liver disease.',
            'died when their knees gave out.' ,
            'fell down, hit their head and died.',
            'slipped on a puddle of gravy, broke their neck and died.',
            'died of degenerative arthritis.',
            'had an infection under a roll and died.',
            'died of dehydration.',
            'broke a leg and had to be put down.'
            ]
    
    def __init__(self):
        print("A wild Fatty appears!\n")
        self.hunting = random.randrange(0,3)
        self.foraging = random.randrange(0,3)
        self.intelligence = random.randrange(0,2)
        self.hunger = 10
        self.max_hunger = 10
        self.max_hp = 10
        self.hp = 10
        self.dead = 0
        self.sex = self.sexes[random.randrange(0,2)]
        self.firstname = self.names[self.sex][random.randrange(0, len(self.names[self.sex]))]
        self.lastname = self.names['last'][random.randrange(0, len(self.names['last']))]
        self.bmi = 0
        # height in inches^2 / weight in lbs * 703
        # bmi
        #   < 18 underweight  
        #   < 18.5 thin for height
        #   18.6 - 24.9 ideal
        #   25 - 29.9 overweight
        #   > 30 obese
        

    def talk(self):
        should_talk = random.randrange(0,5)

        if should_talk == 3:
            fatty_saying = random.randrange(0, len(self.sayings))
            print("\n" + self.firstname + " " + self.lastname + " sez: " + self.sayings[fatty_saying] + "\n")

    def search_for_food(self):
        search = random.randrange(0,10)
        if (search + self.hunting > 7):
            food = random.randrange(0,3)
        else:
            food = 0

        self.hunger += food

        #print("Fatty found " + str(food) + " units of food.")
        
    def debug(self):
        print("Fatty hunting: " + str(self.hunting))
        print("Fatty foraging: " + str(self.foraging))
        print("Fatty intelligence: " + str(self.intelligence))
        print("Fatty hunger: " + str(self.hunger))
        print("Fatty name: " + str(self.name))
        print("\n")

    def deathcause(self):
        return self.deaths[random.randrange(0, len(self.deaths))]
        
