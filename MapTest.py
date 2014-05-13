from MapClass import FMEmap
import array

loc = [2, 5]

test = FMEmap(10, 10)
test.displayHunt()
print
test.displayPlant()
print
loc = test.moveMap(loc, 3)
print
print(test.getHunt(loc))
print
print(test.getPlant(loc))
print
test.displayHunt()
print
test.displayPlant()
print
loc = test.moveMap(loc, 3)
print
print(test.getHunt(loc))
print
print(test.getPlant(loc))
print
test.displayHunt()
print
test.displayPlant()
print
print("Final location: " + str(loc[0]) + "," + str(loc[1]))
