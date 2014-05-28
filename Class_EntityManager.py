class EntityManager(object):
	entities = []

	def __init__(self):
		object.__init__(self)

	def add(self, entity):
		self.entities.append(entity)

	def remove(self, entity):
		self.entities.remove(entity)

	def getAll(self):
		return self.entities

	def update(self):
		pass

