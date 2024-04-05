import endpoint_dicts.races as races
import endpoint_dicts.classes as classes
import important_classes.equipment as equipment
import important_classes.generators as gen
import random

def choose_pack(stat, pack):
            return pack[stat]

class Random_Npc():
    _id_counter = 0

    def choose_race(self):
        race_choice = random.choice(races.RACE_DICT["results"])
        if race_choice["subraces"]:
            subrace_choice = random.choice(list(race_choice["subraces"]))
        else:
            subrace_choice = {
                "index": None,
                "name": None,
                "ability_score_increases": None,
                "skill_proficiencies": None,
                "traits": None
                }

        return race_choice, subrace_choice
    
    def choose_class(self):
         return random.choice(classes.CLASS_DICT["results"])

    def __init__(self):
        Random_Npc._id_counter += 1
        self.id = Random_Npc._id_counter
        self.name = gen.generate_full_name(gen.first_name_elements, gen.last_name_elements)
        self.npc_race, self.npc_subrace = Random_Npc.choose_race(self)
        self.npc_class = Random_Npc.choose_class(self)
        self.npc_class_proficiencies = self.npc_class["proficiencies"]
        self.base_stats = self.set_base_stats()

        print(f"""Name: {self.name}, Race: {self.npc_race["name"]}, Subrace: {self.npc_subrace["name"]}, 
Saving Throws: {self.npc_class_proficiencies["saving_throws"]}
Base Stats: {self.base_stats}""")
        
    def set_base_stats(self):
            base_stats = {"STR": 8, "DEX": 8, "CON": 8, "INT": 8, "WIS": 8, "CHA": 8}
            for stat in base_stats:
                  if stat in self.npc_class_proficiencies["saving_throws"]:
                        base_stats[stat] += 2
            return base_stats

def create_random_npc(num):
     for i in range(num):
          Random_Npc()

create_random_npc(1)