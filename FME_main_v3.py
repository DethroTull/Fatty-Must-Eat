from Class_Fatty_v2 import Fatty

import random
import array

grid_x = 5
grid_y = 5
max_fatty = 3
max_day = 3
pos_x = random.randrange(0,grid_x)
pos_y = random.randrange(0,grid_y)
food_found = 0

grid_forage = [[0 for x in xrange(grid_x)] for x in xrange(grid_y)]
#print(grid_forage)
grid_hunt = [[0 for x in xrange(grid_x)] for x in xrange(grid_y)]

cgx = 0
while cgx < grid_x:
    cgy = 0
    while cgy < grid_y:
        grid_forage[cgx][cgy] = random.randrange(1,4)
        cgy += 1
    cgx += 1
#print(grid_forage)

cgx = 0
while cgx < grid_x:
    cgy = 0
    while cgy < grid_y:
        grid_hunt[cgx][cgy] = random.randrange(1,4)
        cgy += 1
    cgx += 1
#print(grid_hunt)

def intResolv(i):
    int_r = (random.randrange(0,10) + i)
    print("Int roll: " + str(int_r))
    if int_r > 4:
        return 1
    else:
        return 0

def foodResolv(f):
    food_f = (random.randrange(0,10) + f)
    print("Food roll: " + str(food_f))
    if food_f > 7:
        return 1
    else:
        return 0

fatty1 = Fatty()
print("MP: " + str(fatty1.max_ap))
print("Int: " + str(fatty1.int))
print("Forage: " + str(fatty1.foraging))
print("Hunt: " + str(fatty1.foraging))
print("Starting location: " + str(pos_x) + "," + str(pos_y))

cd = 0
while cd < max_day:
    cm = 0
    print("Day #" + str(cd+1))
    while cm < fatty1.max_ap:
        move = random.randrange(0,4)
        print("Move #" + str(cm + 1))
        print("Move Roll: " + str(move))
        if move == 0:
            if pos_x > 0 and pos_x < grid_x:
                pos_x -= 1
                print("Up 1")
            else:
                print("Bump top!")
        if move == 1:
            if pos_y > -1 and pos_y < (grid_y - 1):
                pos_y += 1
                print("Right 1")
            else:
                print("Bump right!")
        if move == 2:
            if pos_x > -1 and pos_x < (grid_x - 1):
                pos_x += 1
                print("Down 1")
            else:
                print("Bump down!")
        if move == 3:
            if pos_y > 0 and pos_y < grid_y:
                pos_y -= 1
                print("Left 1")
            else:
                print("Bump left!")
        cm += 1
    print("Current Location: " + str(pos_x) + "," + str(pos_y))
    print("Forage: " + str(grid_forage[pos_x][pos_y]) + " Hunting: " +
          str(grid_hunt[pos_x][pos_y]))
    choice = intResolv(fatty1.int)
    print("Choice resolution: " + str(choice))
    if choice == 1:
        print("Int check success!")
        if fatty1.foraging > fatty1.hunting:
            food_forage = foodResolv(fatty1.foraging)
            if food_forage == 1:
                food_found = grid_forage[pos_x][pos_y]
                print("Fatty foraged " + str(food_found) + " unit(s) of food.")
            else:
                food_found = 0
                print("Fatty foraging failed.")
        else:
            food_hunt = foodResolv(fatty1.hunting)
            if food_hunt == 1:
                food_found = grid_hunt[pos_x][pos_y]
                print("Fatty hunted " + str(food_found) + " unit(s) of food.")
            else:
                food_found = 0
                print("Fatty hunting failed.")
    else:
        print("Int check failed!")
        food_random = random.randrange(0,3)
        if food_random == 1:
            food_forage = foodResolv(fatty1.foraging)
            if food_forage == 1:
                food_found = grid_forage[pos_x][pos_y]
                print("Fatty foraged " + str(food_found) + " unit(s) of food.")
            else:
                food_found = 0
                print("Fatty foraging failed.")
        elif food_random == 0:
            food_hunt = foodResolv(fatty1.hunting)
            if food_hunt == 1:
                food_found = grid_hunt[pos_x][pos_y]
                print("Fatty hunted " + str(food_found) + " unit(s) of food.")
            else:
                food_found = 0
                print("Fatty hunting failed.")
        else:
            food_found = 0
            print("Fatty shit his pants.")
    cd += 1

print("DONE!")
    
    
    
