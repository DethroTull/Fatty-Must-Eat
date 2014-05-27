import time
import random
import array
import csv
import os
import sys
import platform
import json
import uuid
from Class_Fatty import Fatty
#from MapClass import FMEmap
from DisasterClass import Disaster
from Class_Animal import Animal

class EntityFactory(object):

	def __init__(self):
		pass

	def createEntity(self, entityType, max_x, max_y, statJson = ""):
		if entityType == "fatty":
			tempEntity = Fatty(uuid.uuid4(), max_x, max_y )
		elif entityType == "animal":
			animalKeys = statJson.keys()
			animalType = animalKeys[random.randrange(0, len(animalKeys))]
			tempEntity = Animal(uuid.uuid4(), max_x, max_y, statJson[animalType])
		elif entityType == "deity":
			# To DO
			pass
		elif entityType == "disaster":
			# To DO
			pass

		print("created: " + tempEntity.fullname)
		return tempEntity
