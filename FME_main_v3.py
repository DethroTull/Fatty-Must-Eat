from Class_Fatty_v2 import Fatty

import random
import array

grid_x = 5
grid_y = 5
max_fatty = 5
max_day = 10
pos_x = random.randrange(0,grid_x)
pos_y = random.randrange(0,grid_y)
food_found = 0
pst = 0

log = open("c:/FME/FME_log_v2.txt", "w") #Open log file

#Grid init
grid_forage = [[0 for x in xrange(grid_x)] for x in xrange(grid_y)] #forage grid
#print(grid_forage)
grid_hunt = [[0 for x in xrange(grid_x)] for x in xrange(grid_y)] #hunting grid

#Init fatty array
fatty_array = []
for i in range(max_fatty): #Populate fatty array with fatties
    temp_fatty = Fatty()
    fatty_array.append(temp_fatty)

#assign grid values
log.write("Forage Grid\n")
cgx = 0
while cgx < grid_x:
    cgy = 0
    while cgy < grid_y:
        grid_forage[cgx][cgy] = random.randrange(1,4)
        log.write(str(grid_forage[cgx][cgy]) + " ")
        cgy += 1
    log.write("\n")
    cgx += 1
#print(grid_forage)

log.write("\nHunting Grid\n")
cgx = 0
while cgx < grid_x:
    cgy = 0
    while cgy < grid_y:
        grid_hunt[cgx][cgy] = random.randrange(1,4)
        log.write(str(grid_hunt[cgx][cgy]) + " ")
        cgy += 1
    log.write("\n")
    cgx += 1
#print(grid_hunt)

def intResolv(i):
    int_r = (random.randrange(0,10) + i)
    log.write("Int roll: " + str(int_r) + "\n")
    if int_r > 4:
        return 1
    else:
        return 0

def foodResolv(f):
    food_f = (random.randrange(0,10) + f)
    log.write("Food roll: " + str(food_f) + "\n")
    if food_f > 7:
        return 1
    else:
        return 0


print
cfat = 1
for fatty in fatty_array:
    log.write("\nFatty #" + str(cfat))
    log.write("\nMP: " + str(fatty.max_ap))
    log.write("\nInt: " + str(fatty.int))
    log.write("\nForage: " + str(fatty.foraging))
    log.write("\nHunt: " + str(fatty.foraging))
    log.write("\nStarting location: " + str(pos_x) + "," + str(pos_y) + "\n")
    cfat += 1

#fatty1 = Fatty()
    
#print("MP: " + str(fatty1.max_ap))
#print("Int: " + str(fatty1.int))
#print("Forage: " + str(fatty1.foraging))
#print("Hunt: " + str(fatty1.foraging))
#print("Starting location: " + str(pos_x) + "," + str(pos_y))

cd = 0
cfat = 1
while cd < max_day:
    cm = 0
    print("Day #" + str(cd+1) + "\n")
    log.write("\nDay #" + str(cd+1) + "\n")
    for fatty in fatty_array:
        print("Fatty #" + str(cfat))
        log.write("Fatty #" + str(cfat) + "\n")
        while cm < fatty.max_ap:
            move = random.randrange(0,4)
            log.write("Move #" + str(cm + 1) + "\n")
            log.write("Move Roll: " + str(move) + "\n")
            if move == 0:
                if pos_x > 0 and pos_x < grid_x:
                    pos_x -= 1
                    log.write("Up 1\n")
                else:
                    log.write("Bump top!\n")
            if move == 1:
                if pos_y > -1 and pos_y < (grid_y - 1):
                    pos_y += 1
                    log.write("Right 1\n")
                else:
                    log.write("Bump right!\n")
            if move == 2:
                if pos_x > -1 and pos_x < (grid_x - 1):
                    pos_x += 1
                    log.write("Down 1\n")
                else:
                    log.write("Bump down!\n")
            if move == 3:
                if pos_y > 0 and pos_y < grid_y:
                    pos_y -= 1
                    log.write("Left 1\n")
                else:
                    log.write("Bump left!\n")
            cm += 1
        log.write("Current Location: " + str(pos_x) + "," + str(pos_y) + "\n")
        log.write("Forage: " + str(grid_forage[pos_x][pos_y]) + " Hunting: " +
              str(grid_hunt[pos_x][pos_y]) + "\n")
        choice = intResolv(fatty.int)
        log.write("Choice resolution: " + str(choice) + "\n")
        if choice == 1:
            log.write("Int check success!\n")
            if fatty.foraging >= fatty.hunting:
                food_forage = foodResolv(fatty.foraging)
                if food_forage == 1:
                    food_found = grid_forage[pos_x][pos_y]
                    print("Fatty foraged " + str(food_found) + " unit(s) of food.\n")
                    log.write("Fatty foraged " + str(food_found) + " unit(s) of food.\n")
                else:
                    food_found = 0
                    print("Fatty foraging failed.\n")
                    log.write("Fatty foraging failed.\n")
            else:
                food_hunt = foodResolv(fatty.hunting)
                if food_hunt == 1:
                    food_found = grid_hunt[pos_x][pos_y]
                    print("Fatty hunted " + str(food_found) + " unit(s) of food.\n")
                    log.write("Fatty hunted " + str(food_found) + " unit(s) of food.\n")
                else:
                    food_found = 0
                    print("Fatty hunting failed.\n")
                    log.write("Fatty hunting failed.\n")
        else:
            log.write("Int check failed!\n")
            food_random = random.randrange(0,3)
            if food_random == 1:
                food_forage = foodResolv(fatty.foraging)
                if food_forage == 1:
                    food_found = grid_forage[pos_x][pos_y]
                    print("Fatty foraged " + str(food_found) + " unit(s) of food.\n")
                    log.write("Fatty foraged " + str(food_found) + " unit(s) of food.\n")
                else:
                    food_found = 0
                    print("Fatty foraging failed.\n")
                    log.write("Fatty foraging failed.\n")
            elif food_random == 0:
                food_hunt = foodResolv(fatty.hunting)
                if food_hunt == 1:
                    food_found = grid_hunt[pos_x][pos_y]
                    print("Fatty hunted " + str(food_found) + " unit(s) of food.\n")
                    log.write("Fatty hunted " + str(food_found) + " unit(s) of food.\n")
                else:
                    food_found = 0
                    print("Fatty hunting failed.\n")
                    log.write("Fatty hunting failed.\n")
            else:
                food_found = 0
                print("Fatty shit his pants.\n")
                log.write("Fatty shit his pants.\n")
                pst += 1
        log.write(" ")
        cfat += 1
        cm = 0
    cfat = 1
    cd += 1

print("DONE!")
print("Drawers were filled a total of " + str(pst) + " times!")
log.write ("\nDrawers were filled a total of " + str(pst) + " times!\n")
log.close()
    
    
    
