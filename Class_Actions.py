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

    def update(self):
        entities = self.entityManager.getAll()
        for entity in entities:
            if entity.dead == 0:
                self.hunger(entity)
                print(entity.fullname + " Current Calorie Count: " + str(entity.calories))
                
