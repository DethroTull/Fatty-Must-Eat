from Class_Moveable import Moveable
import uuid
import random

#The Fatty Class needs to have a max x/y when generatated.
#   This will allow the initial location of the fatty to stay within the grid.
class Fatty(Moveable):
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
    
    def __init__(self, max_x, max_y):
        self.id = uuid.uuid4()
        self.type = "fatty"
        self.max_x = max_x #maximum rows for the grid
        self.max_y = max_y #maximum columns for the grid
        self.location = [random.randrange(0,self.max_x),random.randrange(0,self.max_y)] #random starting location
        self.mp = random.randrange(1,3) #movement points
        self.hunting = random.randrange(0,10) #hunting skill
        self.foraging = random.randrange(0,10) #foraging skill
        self.intelligence = random.randrange(0,2) #intelligence skill
        self.max_calories = 2000
        self.calories = 2000
        self.hunger_ratio = 20
        self.max_hp = 10
        self.hp = 10
        self.dead = 0
        self.sex = self.sexes[random.randrange(0,2)]
        self.firstname = self.names[self.sex][random.randrange(0, len(self.names[self.sex]))]
        if(self.firstname == "Shawn"):
            self.firstname = "Comrade Commissar Shawn"
            self.lastname = "Willick"
        else:
            self.lastname = self.names['last'][random.randrange(0, len(self.names['last']))]
        self.fullname = self.firstname + " " + self.lastname
        self.bmi = 0
        self.days_alive = 0
        self.awareness = random.randrange(0,5)
        self.hiding = 0
        self.aggression = random.randrange(0,5)
        self.pain_resistance = random.randrange(0,5)
        self.luck = 0
        self.age = 0
        self.agility = random.randrange(1,10)
        self.dodge = random.randrange(1,5)
        self.dexterity = 0
        self.strength = random.randrange(1, 5)
        self.food = 400
        self.food_type = 1 #1 for hunter, 2 for grazer
        if self.lastname == "Willick":
            self.has_special = 2
            self.special = self.fullname + " calls down the power of the proletariat to smite the enemies of The Party!"
        else:
            self.has_special = 0

        # Physical (combat, athletics, sports, all of that)
        # Mental (purely intellectual stuff, knowledge, analysis)
        # Social (persuasion, languages, acting etc)
        # Practical (this covered arts, crafts, mechanics and maintenance, driving, etc)

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
            print("\n" + self.firstname + " " + self.lastname + " [HP:" + str(self.hp) + "/" + str(self.max_hp) + "] sez: " + self.sayings[fatty_saying] + "\n")

    #hunting function which takes the food amount supplied to the function
    def huntFood(self, f):
        search = random.randrange(0,10)
        if (search + self.hunting > 7): #use the hunting skill to modify the hunt RNG
            food = f #if the hunt is successful assign food from an outside source
        else:
            food = 0 #if the hunt is unsuccessful no food is found

        self.hunger += food #increase the hunger count by the amount of food found
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger #does not allow the hunger count above max hunger

    #foraging fuction which takes the food amount supplied to the function
    def forageFood(self, f):
        search = random.randrange(0,10)
        if (search + self.foraging > 7): #use the foraginging skill to modify the forage RNG
            food = f #if the forage is successful assign food from an outside source
        else:
            food = 0 #if the hunt is unsuccessful no food is found

        self.hunger += food #increase the hunger count by the amount of food found
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger #does not allow the hunger count above max hunger

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


    def update(self, day_count):
        self.talk()


    # def attack(self, attackee):
    #     if attackee.awareness > self.awareness:
    #         chance_to_hide = random.randrange(0,5)
    #         if chance_to_hide == 4:
    #             print(self.fullname + " lost track of " + attackee.fullname + ". Where could they have went?")
    #             return
    #         else:
    #             print(self.fullname + " missed " + attackee.fullname + ".")
    #     elif self.agility > attackee.dodge:
    #         damage = random.randrange(1,3)
    #         attackee.hp -= damage
    #         print(self.fullname + " hit " + attackee.fullname + " for " + str(damage) + " damage.  Ouch!")
    #     else:
    #         print(self.fullname + " missed " + attackee.fullname + ".")


    # def somefunc(self):
    #     Moveable.somefunc(self)
