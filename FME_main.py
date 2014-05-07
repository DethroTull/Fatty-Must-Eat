#Fatty Must Eat Version 0.0021
import time
import random
import array
import csv
import os
import sys

log = open("c:/FME/FME_log.txt", "w") #open log file
importfilename = "c:/FME/fatty_conf.csv"

if os.path.isfile(importfilename):
    fme_conf = open(importfilename, 'r') #open the configuration file
else:    
    print(importfilename + " doesn't exist. How else will we know how many fatties need to eat?")
    log.close()
    sys.exit()


fme_csv = csv.reader(fme_conf) #init csv reader
#assign total fatties and max hunger from csv file
for row in fme_csv:
    d = row[1]
    h = row[3]
    hp = row[5]

#User input for number of dudes
#d = raw_input("Enter total number of fatties: ")
#print

#Array generation
array_max = int(d)
dude_hunger_skill = array.array('i', xrange(array_max))
dude_age = array.array('i', xrange(array_max))
dude_int_skill = array.array('i', xrange(array_max))

#function foodSearch argument hunger_skill
def foodSearch(h):
    fsearch = random.randrange(0, 10)
    if (fsearch + h) > 7:
        food = random.randrange(1, 4)
    else:
        food = 0
    return food

c1 = 0 #hunger_skill counter
c2 = 0 #dude simulator counter
c3 = 0 #age output counter
c4 = 0 #int_skill counter

max_hunger = int(h)
hp_max = int(hp)


log.write("Total Fatties: " + d)
log.write("\nMax Hunger: " + str(max_hunger) + "\n")

#hunger_skill assignment
while c1 < array_max:
    dude_hunger_skill[c1] = random.randrange(0, 3)
    print("Fatty #" + str(c1 + 1) + " Hunger Skill: " +  str(dude_hunger_skill[c1]))
    log.write("\nFatty #" + str(c1 + 1) + " Hunger Skill: " +  str(dude_hunger_skill[c1]) + "\n")
    c1 += 1

while c4 < array_max:
    dude_int_skill[c4] = random.randrange(0,2)
    print("Fatty #" + str(c4 + 1) + " Int Skill: " + str(dude_int_skill[c4]))
    log.write("Fatty #" + str(c4 + 1) + " Int Skill: " + str(dude_int_skill[c4]) + "\n")
    c4 += 1
      

#Daily calculations for fatties
while c2 < array_max:
    dead = 0
    day = 0
    hunger = max_hunger
    t0 = time.time()
    fatty_hp = hp_max
    
    print("\nFatty #" + str(c2 + 1) + " calculating")
    log.write("\n")
    log.write("\nFatty #" + str(c2 +1))
    
    while dead == 0 and day < 100:
        t1 = time.time()

        if (t1 - t0) >= 2.0: #Each day is X.X seconds
            food_found = foodSearch(dude_hunger_skill[c2])
            hunger = hunger + food_found
            if hunger > max_hunger:
                hunger = max_hunger
            log.write("\nDay " + str(day + 1) + " Hunger " + str(hunger))
            log.write("\nYou found " + str(food_found) + " units of food") 
            hunger -= 1
            day += 1
            if hunger <= 0:
                fatty_hp -= 1
            log.write("\nHP: " + str(fatty_hp) +"\n")
            if fatty_hp <= 0:
                dead = 1
    
    dude_age[c2] = day
    c2 += 1

print
while c3 < array_max:
    print("Fatty #" + str(c3 + 1) + " lasted: " + str(dude_age[c3]) + " days")
    log.write("\nFatty #" + str(c3 + 1) + " lasted: " + str(dude_age[c3]) + " days")
    c3 += 1

log.close()
fme_conf.close()





