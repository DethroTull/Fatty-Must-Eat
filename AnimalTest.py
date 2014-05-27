from Class_Animal import Animal
import json


animal_stat_json = json.load(open("FME_animals.json"))

a1 = Animal(0, 1, 1, animal_stat_json)

