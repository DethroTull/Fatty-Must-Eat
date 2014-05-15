from DisasterClass import Disaster

poop = Disaster(5,5)

d = poop.genDisaster()
print(d)
print

t = poop.getTornado()
print (t[0] + " stats")
print ("Starting location: " + str(t[1]) + "," + str(t[2]))
print ("Movement points: " + str(t[3]))
print ("Destruction modifier: " + str(t[4]))
print ("Length in days: " + str(t[5]))
print

fa = poop.getFamine()
print (fa[0] + " stats")
print ("Food modifier: " + str(fa[1]))
print ("Length in days: " + str(fa[2]))
print

fl = poop.getFlood()
print (fl[0] + " stats")
print ("Food modifier: " + str(fl[1]))
print ("Length in days: " + str(fl[2]))
print
