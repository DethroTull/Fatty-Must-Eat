#Fatty Must Eat configuration file generator 0.0001
#Writing main variables to a csv file
#Uses c:\FME for the directory

fatty_conf = open("c:/FME/fatty_conf.csv", "w") #Open the csv file

#input for main variables
fatty_total = raw_input("Enter total number of fatties: ") 
hunger_max = raw_input("Enter max hunger level: ")
hp_max = raw_input("Enter max hitpoints: ")
grid_x = raw_input("Enter map 'x' max: ")
grid_y = raw_input("Enter map 'y' max: ")

#Writing the variables to the csv file
fatty_conf.write("fatty_total," + fatty_total)
fatty_conf.write(",hunger_max," + hunger_max)
fatty_conf.write(",hp_max," + hp_max)
fatty_conf.write(",grid_x," + grid_x)
fatty_conf.write(",grid_y," + grid_y)

fatty_conf.close() #Close the csv file
