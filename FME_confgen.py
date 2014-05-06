#Fatty Must Eat configuration file generator 0.0001
#Writing main variables to a csv file

fatty_conf = open("fatty_conf.csv", "w") #Open the csv file

#input for main variables
fatty_total = raw_input("Enter total number of fatties: ") 
hunger_max = raw_input("Enter max hunger level: ")

#Writing the variables to the csv file
fatty_conf.write("fatty_total," + fatty_total + "," + "hunger_max," + hunger_max)

fatty_conf.close() #Close the csv file
