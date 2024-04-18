from npc import *
import important_classes.generators as gen
import random

class Area():
    def __init__(self):
        self.set_population()
        self.generate_npcs()
        self.generate_buildings()
        self.set_npc_jobs()

    def set_population(self):
        self.population = random.randint(0, 5)

    def generate_npcs(self):
        self.npcs = create_town_dump(self.population)

    def generate_job_board(self):
        noble_npcs = round(0.03 * self.population)
        guard_npcs = round(0.12 * self.population)
        unemployed_npcs = round(0.06 * self.population)
        retired_npcs = round(0.08 * self.population)
        business_owner_npcs = round(0.09 * self.population)
        adventurer_npcs = round(0.06 * self.population)
        mercenary_npcs = round(0.06 * self.population)
        worker_npcs = round(0.50 * self.population)
        
        # Check if the total matches the population
        total_npcs = (noble_npcs + guard_npcs + unemployed_npcs + retired_npcs +
                    business_owner_npcs + adventurer_npcs + mercenary_npcs + worker_npcs)
        
        # adjust to meet total population exactly
        discrepancy = self.population - total_npcs
        worker_npcs += discrepancy

        job_counts = {
            "noble": noble_npcs,
            "guard": guard_npcs,
            "unemployed": unemployed_npcs,
            "retired": retired_npcs,
            "business_owner": business_owner_npcs,
            "adventurer": adventurer_npcs,
            "mercenary": mercenary_npcs,
            "worker": worker_npcs
        }
        return job_counts
    
    def generate_buildings(self, objClass):
        pass

    def set_npc_jobs(self):
        job_counts = self.generate_job_board()
        updated_npcs = []

        for npc in self.npcs["npcs"]:
            if npc.get("job"):
                updated_npcs.append(npc)
            else:
                for job in job_counts:
                    if job_counts[job] > 0:
                        npc["job"] = job
                        npc["owner"] = None
                        npc["home"] = None
                        npc["current_place"] = None
                        npc["relationships"] = []
                        job_counts[job] -= 1
                        updated_npcs.append(npc)
                        break

        self.npcs["npcs"] = updated_npcs

class Hamlet(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(100, 125)

class SmallTown(Area):
    def __init__(self):
        super().__init__()
    
    def set_population(self):
        self.population = random.randint(2000, 2125)



class Building():
    def __init__(self):
        self.generate_name()
    
    def generate_name(self):
        self.building_name = gen.generate_building_name(gen.TAVERN_NAME_ELEMENTS)

    def generate_owner(self):
        pass

class Tavern(Building):
    def __init__(self):
        super().__init__()

x = Hamlet()
print(x.npcs)

for item in range(10):
    tavern = Tavern()
    print(tavern.building_name)