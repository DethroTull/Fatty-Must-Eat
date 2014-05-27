import random

class BattleSystem:

	def __init__(self, entityManager):
		self.entityManager = entityManager

	def attemptAttack(self):
		pass

	def act(self, attackingEntity, defendingEntity):
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
		while True:
			damage_to_enemy = random.randrange(0, attackingEntity.strength)
			damage_from_enemy = random.randrange(0, defendingEntity.strength)
			defendingEntity.hp -= damage_to_enemy
			attackingEntity.hp -= damage_from_enemy

			print("A " + attackingEntity.fullname + " wallops " + defendingEntity.fullname + " for " + str(damage_to_enemy) + " damage.")
			print(defendingEntity.fullname + " pummels " + attackingEntity.fullname + " for " + str(damage_from_enemy) + " damage.")

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

	def update(self):
		pass

	def cleanup(self):
		for entity in self.entities:
			if entity.dead > 0:
				print(entity.fullname + " died.")
