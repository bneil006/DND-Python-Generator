from npc import *
import random

class Area():
    def __init__(self):
        self.set_population()
        self.generate_npcs()
        self.set_npc_jobs()

    def set_population(self):
        self.population = random.randint(0, 5)

    def generate_npcs(self):
        self.npcs = create_town_dump(self.population)

    def generate_buildings(self):
        # 1% should be noble
        # 5% of the population should be guards
        # 7% should be unemployeed
        # 8% should be retired
        # 9% should be business owners
        # 10% should be adventurers
        # 10% should be mercenaries
        # 50% should be workers

        noble_npcs, guard_npcs, unemployeed_npcs, retired_npcs = 0, 0, 0, 0
        business_owner_npcs, adventurer_npcs, mercenary_npcs, worker_npcs = 0, 0, 0, 0
        pass

    def set_npc_jobs(self):
        updated_npcs = []
        for npc in self.npcs["npcs"]:
            npc_addition = {
                "job": "Blacksmith"
            }
            updated_npcs.append({**npc, **npc_addition})
        self.npcs["npcs"] = updated_npcs


            

class Hamlet(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(1, 3)

print(Hamlet().npcs)