from Class_Moveable import Moveable
import random

class Animal(Moveable):
#                '' : {
#                		'aggressive' : ,
#                		'hp' : {'min' : , 'max' : },
#                		'mp' :,
#                		'dead' : ,
#                		'location' : {'x' : , 'y' :}
#                	 },
#                }

	animal_types = ['wolf', 'chicken']
	animal_type_stats = {
                'wolf' : {
                		'aggressive' : 1,
                		'hp' : {'min' : 10, 'max' : 15},
                		'mp' : 2,
                		'dead' : 0,
                		'location' : {'x' : 3, 'y' : 3},
                		'food' : 2,
                		'max_hunger' : 30,
                		'hunger' : 30,
                		'hunger_ratio' : 1

                	 },
                'chicken' : {
                		'aggressive' : 0,
                		'hp' : {'min' : 2, 'max' : 4},
                		'mp' : 1,
                		'dead' : 0,
                		'location' : {'x' : 1, 'y' : 4},
                		'food' : 2,
                		'max_hunger' : 4,
                		'hunger' : 4,
                		'hunger_ratio' : 1
                	 }
                }

	def __init__(self, sid, max_x, max_y):
		self.id = sid
		self.animal_type = self.animal_types[random.randrange(0,2)]
		self.fullname = self.animal_type + " #" + str(self.id)
		self.aggressive = self.animal_type_stats[self.animal_type]['aggressive']
		self.hp = random.randrange(self.animal_type_stats[self.animal_type]['hp']['min'], self.animal_type_stats[self.animal_type]['hp']['max'])
		self.mp = self.animal_type_stats[self.animal_type]['mp']
		self.dead = 0
		self.location = [self.animal_type_stats[self.animal_type]['location']['x'], self.animal_type_stats[self.animal_type]['location']['y']]
		self.strength = random.randrange(4, 10)
		self.hunger = self.animal_type_stats[self.animal_type]['hunger']
		self.max_hunger = self.animal_type_stats[self.animal_type]['max_hunger']
		self.hunger_ratio = self.animal_type_stats[self.animal_type]['hunger_ratio']
	def talk(self):
		pass

	def attack(self, bar):
		attack_cycles = 0
		while True:
			damage_to_enemy = random.randrange(0, self.strength)
			damage_from_enemy = random.randrange(0, bar.strength)
			bar.hp -= damage_to_enemy
			self.hp -= damage_from_enemy

			print("A " + self.fullname + " wallops " + bar.fullname + " for " + str(damage_to_enemy) + " damage.")
			print(bar.fullname + " pummels " + self.fullname + " for " + str(damage_from_enemy) + " damage.")

			if attack_cycles >= 20:
				print
				print("RA tires of this charade.  Die, " + bar.fullname + ".  Die, " + self.fullname + ".")
				print("RA burns " + self.fullname + " with his holy fire. 99999999 damage.")
				print("RA engulfs " + bar.fullname + " in white hot light. 99999999 damage.")
				print(bar.fullname + " was reduced to the atomic level.")
				print(self.fullname + " has been turned to ash.")

				bar.hp = 0
				self.hp = 0

			if bar.hp <= 0:
				print(bar.fullname + " died.")
				bar.dead = 1
				break
			elif self.hp <= 0:
				self.dead = 1
				break

			attack_cycles += 1

	def debug(self):
		pass

	def deathcause(self):
		pass 
 
        
