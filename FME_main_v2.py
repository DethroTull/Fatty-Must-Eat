import time
import random
import array
import csv
import os
import sys
import platform

from Class_Fatty import Fatty


if(os.name == "posix" and platform.system() == "Darwin"):
    logfilename = "FME_log.txt"
    importfilename = "fatty_conf.csv"
elif (os.name == "nt"):
    logfilename = "c:/FME/FME_log.txt"
    importfilename = "c:/FME/fatty_conf.csv"

log = open(logfilename, "w") #open log file

if os.path.isfile(importfilename):
    fme_conf = open(importfilename, 'r') #open the configuration file
else:    
    print(importfilename + " doesn't exist. How else will we know how many fatties need to eat?")
    log.close()
    sys.exit()


fme_csv = csv.reader(fme_conf) #init csv reader
#assign total fatties and max hunger from csv file
for row in fme_csv:
    num_fatties = 5
    max_hunger = 10
    max_hp = 10

# empty list of fatties
fatty_array = []
total_days = 20
day_count = 1


# create a fatty, and add him to the list
for i in range(num_fatties):
    temp_fatty = Fatty()
    fatty_array.append(temp_fatty)

while day_count <= total_days:
    print("Day of Fat #" + str(day_count) + " begins.")
    t0 = time.time()
    dead = 0
    fatty_count = 0 

    for fatty in fatty_array:
        if(fatty.dead == 0):
            fatty.talk()
            #print("Fatty " + str(fatty_count) + " is looking for food")
            fatty.search_for_food()
            fatty.hunger -= 1
            if(fatty.hunger < 1):
                fatty.dead = 1
                print(fatty.firstname + " " + fatty.lastname + " died of starvation.")

            elif(fatty.hp < 1):
                fatty.dead = 1
                print(fatty.firstname + " " + fatty.lastname + " " + fatty.deathcause())

            fatty.days_alive += 1
        #else:
            #print(fatty.fullname + " is dead.") 

        if(random.randrange(0,10) >= 8):
            fatty.hp = 0
            
        fatty_count += 1

    day_count += 1

print("\n")
for fatty in fatty_array:
    print(fatty.fullname + " lived " + str(fatty.days_alive) + " days.")
log.close()
fme_conf.close()
