import random

class Fatty:
    """ This is the main Fatty class """
    sayings = ['Butter!  Fatty want butter!',
               'Feeeed mmmmeeeeeee!',
               'Dis look tasty to fatty!',
               'Fatty want more food.',
               'I like to put crisco on everything.',
               'Do you like ranch? I do.',
               'Diet coke has 1 calorie.',
               'I might have diabetes.',
               'I\'m not fat I have a glandular problem.',
               'This pizza needs more ranch.',
               'I am made of pudding.']
    names = {'man' : ['Randy', 'Ronald', 'Donald', 'Bert', 'Jim', 'Shawn', 'Alex', 'Paulie', 'Bill', 'Owen'],
             'woman' : ['Bertha', 'Rosie', 'Trudy', 'Edith', 'Edna', 'Helga', 'Olga', 'Denise', 'Shelby', 'Kristie', 'Shawna', 'La Keisha', 'Cinnamon', 'Joannie'],
             'last' : ['Solbstrom', 'Criscoburg', 'Fatstein', 'Slobsky', 'Bean', 'Weiner', 'Butts', 'Butcher', 'Kong', 'McButterpants', 'Heffer', 'The Huge', 'Porcine', 'Rolls', 'O\'Crisco', 'Tubs', 'McFats', 'Von Rolls', 'El Chub']
            }
    sexes = ['man', 'woman']
    pronouns = {
                'man' : { 'possessive' : 'his', 'subjective' : 'he', 'objective' : 'him' },
                'woman' : { 'possessive' : 'her', 'subjective' : 'she', 'objective' : 'her' }
                }
    deaths = ['died from complications related to Type-2 diabetes.',
            'died of a heart attack.',
            'choked on a chicken bone and died.',
            'died of gallbladder cancer.',
            'stroked out and died.',
            'died of fatty liver disease.',
            'died when [possessive] knees gave out.' ,
            'fell down, hit [possessive] head and died.',
            'slipped on a puddle of gravy, broke [possessive] neck and died.',
            'died of degenerative arthritis.',
            'had an infection under a roll and died.',
            'died of dehydration.',
            'broke [possessive] leg and had to be put down.',
            'died when [subjective] sat on a chair and it broke under [possessive] massive girth.'
            ]
    
    def __init__(self):
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
        if(self.firstname == "Shawn"):
            self.lastname = "Willick"
        else:
            self.lastname = self.names['last'][random.randrange(0, len(self.names['last']))]
        self.fullname = self.firstname + " " + self.lastname
        self.bmi = 0
        self.days_alive = 0

        print("A wild Fatty appears!")
        print("Say \"moo\" to " + self.fullname + ".\n")
  #      self.debug()
        # height in inches^2 / weight in lbs * 703
        # bmi
        #   < 18 underweight  
        #   < 18.5 thin for height
        #   18.6 - 24.9 ideal
        #   25 - 29.9 overweight
        #   > 30 obese
        

    def talk(self):
        #print(self.fullname + " hunger: " + str(self.hunger))
        #if(self.hunger <= 1):
#            print(self.firstname + " " + self.lastname + " sez: I'm feeling faint.  Everything is blurry.")
#        elif(self.hunger < 3):
#            print(self.firstname + " " + self.lastname + " sez: I need to feed NOW!")
#        elif(self.hunger < 5):
#            print(self.firstname + " " + self.lastname + " sez: Where is the food?")
#        elif(self.hunger < 7):
#            print(self.firstname + " " + self.lastname + " sez: I'm kinda hungry.")
            
        should_talk = random.randrange(0,25)

        if should_talk == 10:
            fatty_saying = random.randrange(0, len(self.sayings))
            print("\n" + self.firstname + " " + self.lastname + " sez: " + self.sayings[fatty_saying] + "\n")

    def search_for_food(self):
        search = random.randrange(0,10)
        if (search + self.hunting > 7):
            food = random.randrange(0,3)
        else:
            food = 0

        self.hunger += food

        #print(self.fullname + " found " + str(food) + " units of food.")
        
    def debug(self):
        print("Fatty hunting: " + str(self.hunting))
        print("Fatty foraging: " + str(self.foraging))
        print("Fatty intelligence: " + str(self.intelligence))
        print("Fatty hunger: " + str(self.hunger))
        print("Fatty name: " + str(self.firstname) + " " + self.lastname)
        print("\n")

    def deathcause(self):
        deathtext = self.deaths[random.randrange(0, len(self.deaths))]
        deathtext = deathtext.replace("[possessive]", self.pronouns[self.sex]['possessive'])
        deathtext = deathtext.replace("[subjective]", self.pronouns[self.sex]['subjective'])
        deathtext = deathtext.replace("[objective]", self.pronouns[self.sex]['objective'])
        return deathtext
        
