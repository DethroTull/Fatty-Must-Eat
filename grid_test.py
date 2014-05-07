import random
import array

#base grid generation
grid_x = 3 #total columns
grid_y = 3 #total rows
grid = [[0 for x in xrange(grid_x)] for x in xrange(grid_y)] #array to store the grid

#populate the grid with random food values
cx = 0

while cx < grid_x:
    cy = 0
    while cy < grid_y:
        grid[cx][cy] = random.randrange(0,4)
        cy += 1
    cx += 1

print(grid)
print

#random starting location
start_x = random.randrange(0,grid_x)
start_y = random.randrange(0,grid_y)

day_total = 11 #total time to run the simulation

#simulation run loop
cd = 0
position_x = start_x
position_y = start_y

while cd < day_total:
    print("Day: " + str(cd + 1))
    print("Location: " + str(position_x) + "," + str(position_y))
    print("Food Found: " + str(grid[position_x][position_y]) + "\n")

    move = random.randrange(0,4)
    print("Move = " + str(move) + "\n")

    if move == 0:
        if position_x > 0 and position_x < grid_x:
            position_x -= 1

    if move == 1:
        if position_y > -1 and position_y < (grid_y - 1):
            position_y += 1

    if move == 2:
        if position_x > -1 and position_x < (grid_x - 1):
            position_x += 1
    
    if move == 3:
        if position_y > 0 and position_y < grid_y:
            position_y -= 1

    cd += 1

print("Simulation complete!")
