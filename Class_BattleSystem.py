import random

class BattleSystem:

	def __init__(self, entityManager, grid):
		self.entityManager = entityManager
		self.grid = grid

	def attemptAttack(self, attackingEntity, defendingEntity):
        # if defendingEntity.awareness > attackingEntity.awareness:
        #     chance_to_hide = random.randrange(0,5)
        #     if chance_to_hide == 4:
        #         print(attackingEntity.fullname + " lost track of " + defendingEntity.fullname + ". Where could they have went?")
        #         return
        #     else:
        #         print(attackingEntity.fullname + " missed " + defendingEntity.fullname + ".")
        # elif attackingEntity.agility > defendingEntity.dodge:
        #     damage = random.randrange(1,3)
        #     defendingEntity.hp -= damage
        #     print(attackingEntity.fullname + " hit " + defendingEntity.fullname + " for " + str(damage) + " damage.  Ouch!")
        # else:
        #     print(attackingEntity.fullname + " missed " + defendingEntity.fullname + ".")
		attack_cycles = 0
		special_attack = 0
                print
                print (attackingEntity.fullname + " and " + defendingEntity.fullname + " get into a scuffle!")
		while True:
                        sa_random = random.randrange(0, 20)
                        if sa_random > 17 and attackingEntity.has_special == 1:
                                print ("Critical Attack!")
                                print (attackingEntity.special)
                                print (attackingEntity.fullname + " destroyed " + defendingEntity.fullname)
                                defendingEntity.hp = 0
                        else:
                                damage_to_enemy = random.randrange(0, attackingEntity.strength)
                                damage_from_enemy = random.randrange(0, defendingEntity.strength)

                                print("A " + attackingEntity.fullname + " [HP:" + str(attackingEntity.hp) + "/" + str(attackingEntity.max_hp) + "]" + " wallops " + defendingEntity.fullname + " for " + str(damage_to_enemy) + " damage.")
                                print(defendingEntity.fullname + " [HP:" + str(defendingEntity.hp) + "/" + str(defendingEntity.max_hp) + "]" + " pummels " + attackingEntity.fullname + " for " + str(damage_from_enemy) + " damage.")

                                defendingEntity.hp -= damage_to_enemy
                                attackingEntity.hp -= damage_from_enemy

			if attack_cycles >= 20:
				print
				print("RA tires of this charade.  Die, " + defendingEntity.fullname + ".  Die, " + attackingEntity.fullname + ".")
				print("RA burns " + attackingEntity.fullname + " with his holy fire. 99999999 damage.")
				print("RA engulfs " + defendingEntity.fullname + " in white hot light. 99999999 damage.")
				print(defendingEntity.fullname + " was reduced to the atomic level.")
				print(attackingEntity.fullname + " has been turned to ash.")

				defendingEntity.hp = 0
				attackingEntity.hp = 0

			if defendingEntity.hp <= 0:
				print(defendingEntity.fullname + " died.")
				defendingEntity.dead = 1
				print(attackingEntity.fullname + " dines on dead " + defendingEntity.fullname + " and eats " + str(defendingEntity.food) + " units.")
				attackingEntity.hunger += defendingEntity.food
				break
			elif attackingEntity.hp <= 0:
				print (attackingEntity.fullname + " died.")
				attackingEntity.dead = 1
				print(defendingEntity.fullname + " dines on dead " + attackingEntity.fullname + " and eats " + str(attackingEntity.food) + " units.")
				defendingEntity.hunger += attackingEntity.food
				break

			attack_cycles += 1

	def act(self, attackingEntity, defendingEntity):

		if attackingEntity.type == "fatty":
			if attackingEntity.intelligence == 0:
				print attackingEntity.fullname + " is re-re dumb and is showing an extra chromosome."
			elif attackingEntity.aggression != 0:
				print attackingEntity.fullname + " wants to kill something."
			elif attackingEntity.hunger < (attackingEntity.max_hunger * .3):
				print attackingEntity.fullname + " should find some food."
		for defender in defendingEntity:
			if defender != attackingEntity:
				if defender.dead == 0:
					if attackingEntity.aggression > defender.aggression:	
						self.attemptAttack(attackingEntity, defender)
					else: 
						self.attemptAttack(defender, attackingEntity)

	def update(self):

		entities = self.entityManager.getAll()

		for entity in entities:
			if entity.dead > 0:
				self.entityManager.remove(entity)
			else:
				entity.oldlocation = [entity.location[0], entity.location[1]]
				self.grid.moveEntity(entity)
				if len(self.grid.gridMap[entity.location[0]][entity.location[1]]) > 1:
					self.act(entity, self.grid.gridMap[entity.location[0]][entity.location[1]])
		pass

	def cleanup(self):
		self.grid.displayGrid()
		for entity in self.entities:
			if entity.dead > 0:
				print(entity.fullname + " died.")
