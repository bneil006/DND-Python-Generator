from npc import *
import random

class Area():
    def __init__(self):
        self.set_population()
        self.generate_npcs()

    def set_population(self):
        self.population = random.randint(0, 5)

    def generate_npcs(self):
        self.npcs = create_town_dump(self.population)

    def get_town_information(self):
        for npc in self.npcs["npcs"]:
            print(npc["name"])

class Hamlet(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(80, 120)
    
class SmallTown(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(2000, 2500)


x = Hamlet()
x.get_town_information()