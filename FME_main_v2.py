import time
import random
import array
import csv
import os
import sys
import platform
import json

from Class_FattyContainer import FattyContainer
from Class_AnimalContainer import AnimalContainer
from Class_DeityContainer import DeityContainer
from Class_BattleSystem import BattleSystem
from Class_EntityManager import EntityManager
from Class_EntityFactory import EntityFactory
from Class_Fatty import Fatty
from MapClass import FMEmap
from DisasterClass import Disaster
from Class_Animal import Animal

max_x = 6
max_y = 6

common_items = [
                'rock',
                'stump',
                'tree',
                'bush',
                'dirt',
                'weed',
                'grass',
                'butterfly',
                'breeze',
                'flower',
                'daisy',
                'twig',
                'branch',
                'puddle',
                'mud',
                'stone',
                'babbling brook',
                'river',
                'lake',
                'boulder',
                'excrement',
                'animal remains',
                'bug'
               ]


# empty list of fatties
# fatty_array = []
# animal_array = []
# list_of_dead_fatties = []
# list_of_dead_animals = []
total_days = 20
day_count = 1
num_fatties = 3
num_animals = 9
max_hunger = 10
max_hp = 10
# fatty_id_counter = 0
# animal_id_counter = 0

entityFactory = EntityFactory()

if(os.name == "posix" and platform.system() == "Darwin"):
    logfilename = "FME_log.txt"
    importfilename = "fatty_conf.csv"
    animalsfilename= "FME_animals.json"
elif (os.name == "nt"):
    logfilename = "c:/FME/FME_log.txt"
    importfilename = "c:/FME/fatty_conf.csv"
    animalsfilename = "c:/FME/FME_animals.json" 

log = open(logfilename, "w") #open log file

if os.path.isfile(importfilename):
    fme_conf = open(importfilename, 'r') #open the configuration file
else:    
    print(importfilename + " doesn't exist. How else will we know how many fatties need to eat?")
    log.close()
    sys.exit()

if os.path.isfile(animalsfilename):
    animals_json = json.load(open(animalsfilename))
else:
    print(animalsfilename + " doesn't exist. Fatties need to eat.")
    log.close()
    sys.exit()



#fme_csv = csv.reader(fme_conf) #init csv reader
#assign total fatties and max hunger from csv file
#for row in fme_csv:


#map generation
grid = FMEmap(max_x,max_y)

#print maps for hunting and foraging
grid.displayHunt()
print
grid.displayPlant()
print


# while day_count <= total_days:
#     print("--------------------------")
#     print("| Day of Fat #" + str(day_count) + " begins. |")
#     print("--------------------------")
#     t0 = time.time()
#     dead = 0
#     fatty_count = 0 

#     for fatty in fatty_array:
#         if(fatty.dead == 0):
#             fatty.somefunc()
#             fatty.talk()
#             fatty.location = grid.moveMap(fatty.location,fatty.mp)
        
#             # checks for other fatties in the area.  
#             for otherfatty in fatty_array:
#                 if otherfatty.dead == 0:
#                     if otherfatty.fullname != fatty.fullname:
#                         if otherfatty.location == fatty.location:
#                             print (otherfatty.fullname + " sees " + fatty.fullname + " here.")
#                             if otherfatty.aggression > 1:
#                                 otherfatty.attack(fatty)


#             # attempts to find some food
#             f_amount = grid.getHunt(fatty.location)
#             fatty.huntFood(f_amount)

#             # random occurrences for dumb fatties.
#             # if fatty.intelligence == 0:
#             #     chance_to_attack = random.randrange(0,10)
#             #     if chance_to_attack > 7:
#             #         enemy_item = common_items[random.randrange(0, len(common_items))]
#             #         enemy_item_dmg = random.randrange(1, 4)
#             #         print(fatty.fullname + " is done taking shit from this " + enemy_item + ".  Attack!")
#             #         #time.sleep(1)
#             #         print("\"Duhhh take that, " + enemy_item + ".\"\n")
#             #         print(enemy_item + " hits " + fatty.fullname + " for " + str(enemy_item_dmg) + " damage.\n")
#             #         fatty.hp -= enemy_item_dmg
#             #         #time.sleep(1)
#             #         print("\"You fight hard, " + enemy_item + ".\"\n")
#             #         print(fatty.fullname + " takes one from " + enemy_item + " for " + str(enemy_item_dmg) + " damage.\n")
#             #         #time.sleep(1)
#             #         fatty.hp -= enemy_item_dmg
#             #         print("\"Ow. ow.  ow.         ow!!!!\"\n")
#             #         print("A critical attack from " + enemy_item +"! Christ, " + fatty.fullname + " you're pathetic. " + str(enemy_item_dmg) + " damage.\n")
#             #         #time.sleep(1)
#             #         fatty.hp -= enemy_item_dmg
#             #         print("\"Is that all you got, " + enemy_item + "?\"\n")
#             #         print(fatty.fullname + " took a beating.  " + str(enemy_item_dmg) + " damage.\n")
#             #         fatty.hp -= enemy_item_dmg

#             fatty.hunger -= 1
#             if(fatty.hunger < 1 and fatty.dead != 1):
#                 fatty.dead = 1
#                 print(fatty.firstname + " " + fatty.lastname + " died of starvation.")

#             if fatty.hp <= 0 and fatty.dead != 1:
#                 fatty.dead = 1
#                 print(fatty.fullname + " died.")

#             fatty.days_alive += 1
#         #else:
#             #print(fatty.fullname + " is dead.") 

#         #if(random.randrange(0,10) >= 8):
#          #   fatty.hp = 0
            
#         fatty_count += 1

#     for animal in animal_array:

#         if animal.dead == 0:
#             animal.old_location = [animal.location[0], animal.location[1]]
#             animal.location = grid.moveMap(animal.location, animal.mp)
#             print("A " + animal.fullname + " moved from " + str(animal.old_location) + " to " + str(animal.location) + ".")

#             for otheranimal in animal_array:
#                 if otheranimal.dead == 0:
#                     if otheranimal.location == animal.location and otheranimal.id  != animal.id and otheranimal.animal_type != animal.animal_type:
#                         print ("A " + animal.fullname + " notices " + otheranimal.fullname + " is here as well.")
#                         if animal.aggressive == 1:
#                             #animal.attack(otheranimal)
#                             battlesystem.act(animal, otheranimal)
#                         elif otheranimal.aggressive == 1:
#                             otheranimal.attack(animal)

#             for fatty in fatty_array:
#                 if fatty.dead == 0:
#                     if fatty.location == animal.location:
#                         print ("A " + animal.fullname + " notices " + fatty.fullname + " is here as well.")
#                         if animal.aggressive == 1:
#                             animal.attack(fatty)
                                

#             animal.hunger -= animal.hunger_ratio
            
#             if animal.hunger <= 0:
#                 animal.dead = 1
#                 print(animal.fullname + " died of stavation.")

#         if animal.dead > 0:
#             print(animal.fullname + " has been removed from the world.")
#             print(str(len(animal_array)) + " animals left.")
#             animal_array.remove(animal)


#     day_count += 1

# print("\n")
# for fatty in fatty_array:
#     print(fatty.fullname + " lived " + str(fatty.days_alive) + " days.")
# log.close()
# fme_conf.close()

def main():
    day_count = 1

    entityManager = EntityManager()
    battleSystem = BattleSystem(entityManager)
    # create a fatty, and add him to the list
    for i in range(num_fatties):
        entityManager.add(entityFactory.createEntity("fatty", max_x, max_y))

    # create an animal, and add it to the list
    for i in range(num_animals):
        entityManager.add(entityFactory.createEntity("animal", max_x, max_y, animals_json))
        
    while day_count <= total_days:
        print("--------------------------")
        print("| Day of Fat #" + str(day_count) + " begins. |")
        print("--------------------------")

        for entity in entityManager.getAll():
            entity.update(day_count)

        entityManager.update()
        battleSystem.update()

        day_count += 1

if __name__ == "__main__":
    main()
