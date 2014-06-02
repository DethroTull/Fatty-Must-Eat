from Class_Moveable import Moveable
import uuid
import random

class Animal(Moveable):
	
	def __init__(self, max_x, max_y, animal_type_stats):
		self.id = uuid.uuid4()
		self.type = animal_type_stats['animal_type']
		self.fullname = self.type
		self.aggression = animal_type_stats['aggression']
		self.hp = random.randrange(animal_type_stats['hp']['min'], animal_type_stats['hp']['max'])
		self.max_hp = self.hp
		self.mp = animal_type_stats['mp']
		self.dead = 0
		self.food = animal_type_stats['food']
#		self.location = [animal_type_stats['location']['x'], animal_type_stats['location']['y']]
		self.location = [random.randrange(0, max_x), random.randrange(0, max_y)]
		self.strength = random.randrange(4, 10)
		self.hunger = animal_type_stats['hunger']
		self.max_hunger = animal_type_stats['max_hunger']
		self.hunger_ratio = animal_type_stats['hunger_ratio']
                self.has_special = animal_type_stats['has_special']
                self.special = animal_type_stats['special']
		self.old_location = self.location
	def talk(self):
		pass

	def debug(self):
		pass

	def deathcause(self):
		pass 
 
        
