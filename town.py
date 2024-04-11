from npc import *
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
    
    def generate_buildings(self):
        guard_building = 0
        tavern_building = 0
        bakery_building = 0
        small_house_building = 0
        medium_house_building = 0
        large_house_building = 0

        building_counts = {
            "guard_building": 0,
            "tavern_building": 0,
            "bakery_building": 0,
            "small_house_building": 0,
            "medium_house_building": 0,
            "large_house_building": 0,
        }
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
                        job_counts[job] -= 1
                        updated_npcs.append(npc)
                        break

        self.npcs["npcs"] = updated_npcs

class Hamlet(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(100, 125)

    def generate_buildings(self):
        building_counts = {
            "guard_building": {
                "building_count": 1,
                "max_occupants": random.randint(3, 6),
                "has_owner": False,
                "needs_owner": False
            },
            "tavern_building": {
                "building_count": 2,
                "max_occupants": random.randint(8, 15),
                "has_owner": False,
                "needs_owner": True
            },
            "bakery_building": {
                "building_count": 1,
                "max_occupants": random.randint(8, 15),
                "has_owner": False,
                "needs_owner": True
            },
            "small_house_building": {
                "building_count": 1,
                "max_occupants": random.randint(3, 4),
                "has_owner": False,
                "needs_owner": True
            },
            "medium_house_building": {
                "building_count": 1,
                "max_occupants": random.randint(5, 8),
                "has_owner": False,
                "needs_owner": True
            },
            "large_house_building": {
                "building_count": 1,
                "max_occupants": random.randint(12, 15),
                "has_owner": False,
                "needs_owner": True
            },
        }

class SmallTown(Area):
    def __init__(self):
        super().__init__()
    
    def set_population(self):
        self.population = random.randint(2000, 2125)

class Building():
    def __init__(self):
        self.name_list = ["The Wickied Wyvern", "The Ragod Doll", "The Elven Quimper", "The Mystic Rose", "The Golden Goblet Tavern",
                          "The Sapphire Lagoon", "The Bleak Bastion", "The Silent Sentienl", "The Howling Hyena", "The Parched Pirate",
                          "The Echoing Cavern", "The Shrouded Abbey", "The Wandering Wizard"]
    
    def generate_name(self):
        self.building_name = random.choice(list(self.name_list))
        self.name_list.remove(self.building_name)

class Tavern(Building):
    def __init__(self) -> None:
        super().__init__()

print(SmallTown().generate_job_board())