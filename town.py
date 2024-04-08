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


    def set_npc_jobs(self):
        job_counts = self.generate_job_board()
        updated_npcs = []
        for npc in self.npcs["npcs"]:
            for job in job_counts:
                if job_counts[job] > 0:
                    npc_addition = {
                        "job": job
                    }
                    job_counts[job] -= 1
                    updated_npcs.append({**npc, **npc_addition})
        self.npcs["npcs"] = updated_npcs


class Hamlet(Area):
    def __init__(self):
        super().__init__()

    def set_population(self):
        self.population = random.randint(80, 120)

class SmallTown(Area):
    def __init__(self):
        super().__init__()
    
    def set_population(self):
        self.population = random.randint(2000, 2125)

print(SmallTown().npcs)