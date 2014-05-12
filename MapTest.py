from MapClass import FMEmap
import array

test = FMEmap(10,10,1,3,2)
test.displayHunt()
print
test.displayPlant()
print
test.displayLocation()
print
loc = test.getLocation()
print(loc)
print
test.moveMap()
print
test.displayLocation()
print
print(test.getHunt())
print
print(test.getPlant())
