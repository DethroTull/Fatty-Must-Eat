from Class_Moveable import Moveable
import random

class Animal(Moveable):
	
	def __init__(self, sid, max_x, max_y, animal_type_stats):
		self.id = sid
		self.animal_type = animal_type_stats['animal_type']
		self.fullname = self.animal_type + " #" + str(self.id)
		self.aggressive = animal_type_stats['aggressive']
		self.hp = random.randrange(animal_type_stats['hp']['min'], animal_type_stats['hp']['max'])
		self.mp = animal_type_stats['mp']
		self.dead = 0
		self.location = [animal_type_stats['location']['x'], animal_type_stats['location']['y']]
		self.strength = random.randrange(4, 10)
		self.hunger = animal_type_stats['hunger']
		self.max_hunger = animal_type_stats['max_hunger']
		self.hunger_ratio = animal_type_stats['hunger_ratio']
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
 
        
