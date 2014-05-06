#Fatty Must Eat Version 0.0017
#Python 2.7
import time
import random
import array

log = open("FME_log.txt", "w") #open log file

#User input for number of dudes
d = raw_input("Enter total number of fatties: ")
print

#Array generation
array_max = int(d)
dude_hunger_skill = array.array('i', xrange(array_max))
dude_age = array.array('i', xrange(array_max))

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
max_hunger = 10

#hunger_skill assignment
while c1 < array_max:
    dude_hunger_skill[c1] = random.randrange(0, 3)
    print("Fatty #" + str(c1 + 1) + " Hunger Skill: " +  str(dude_hunger_skill[c1]))
    log.write("Fatty #" + str(c1 + 1) + " Hunger Skill: " +  str(dude_hunger_skill[c1]) + "\n")
    c1 += 1

while c2 < array_max:
    dead = 0
    day = 0
    hunger = max_hunger
    t0 = time.time()
    
    print("\nFatty #" + str(c2 + 1) + " calculating")
    log.write("\n")
    log.write("\nFatty #" + str(c2 +1))
    
    while dead == 0 and day < 100:
        t1 = time.time()

        if (t1 - t0) >= 5.0:
            food_found = foodSearch(dude_hunger_skill[c2])
            hunger = hunger + food_found
            if hunger > max_hunger:
                hunger = max_hunger
            log.write("\nDay " + str(day + 1) + " Hunger " + str(hunger))
            log.write("\nYou found " + str(food_found) + " units of food\n") 
            hunger -= 1
            day += 1
            if hunger <= 0:
                dead = 1
    
    dude_age[c2] = day
    c2 += 1

print
while c3 < array_max:
    print("Fatty #" + str(c3 + 1) + " lasted: " + str(dude_age[c3]) + " days")
    log.write("\nFatty #" + str(c3 + 1) + " lasted: " + str(dude_age[c3]) + " days")
    c3 += 1

log.close()





