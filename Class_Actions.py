import random

class Actions:

    def __init__(self, entityManager):
        self.entityManager = entityManager

    def hunger(self, entity):

        if entity.calories > entity.max_calories:
            entity.calories = entity.max_calories
        else:
            entity.calories -= entity.hunger_ratio
        if entity.calories <= 0:
            entity.dead = 1

    def grazing(self, entity):
        found = random.randrange(0,20)

        if found > 16:
            cal = random.randrange(1,4) * 100
            entity.calories += cal
            print(entity.fullname + " grazed on something tasty and consumed " + str(cal) + " calories.")
    
    def update(self):
        entities = self.entityManager.getAll()

        for entity in entities:
            if entity.dead == 0:
                if entity.food_type == 2:
                    self.grazing(entity)

                self.hunger(entity)
                print(entity.fullname + " Current Calorie Count: " + str(entity.calories))
                
