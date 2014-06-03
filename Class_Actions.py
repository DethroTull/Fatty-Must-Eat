class Actions:

    def __init__(self, entityManager):
        self.entityManager = entityManager

    def hunger(self, entity):
        if entity.hunger > entity.max_hunger:
            entity.hunger = entity.max_hunger
        else:
            entity.hunger -= 1
        if entity.hunger <= 0:
            entity.dead = 1

    def update(self):
        entities = self.entityManager.getAll()
        for entity in entities:
            print(entity.fullname + " Hunger: " + str(entity.hunger))
            self.hunger(entity)
