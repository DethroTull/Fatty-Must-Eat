import time
import random
import array
import csv
import os
import sys
from Class_Fatty import Fatty

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
    num_fatties = int(row[1])
    max_hunger = row[3]
    max_hp = row[5]

# empty list of fatties
fatty_array = [] 

# create a fatty, and add him to the list
for i in range(num_fatties):
    temp_fatty = Fatty()
    temp_fatty.hunting = random.randrange(0,3)
    temp_fatty.foraging = random.randrange(0,3)
    temp_fatty.intelligence = random.randrange(0,2)
    temp_fatty.talk()
    fatty_array.append(temp_fatty)


    
log.close()
fme_conf.close()
