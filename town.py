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

    def get_demographic_information(self):
        job_list = ["Retired", "Unemployeed", "Labourer", "Merchant", "Bartender", "Cook", "Blacksmith"]
        demographic_info = {"npcs": []}

        for npc in self.npcs["npcs"]:
            demo_details = {
                "name": npc["name"],
                "race": npc["race"],
                "subrace": npc["subrace"],
                "job": random.choice(list(job_list))
            }
            demographic_info["npcs"].append(demo_details)
        print(demographic_info)

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
x.get_demographic_information()