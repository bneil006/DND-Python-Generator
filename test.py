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
    
    def choose_level(self):
          return random.randint(1, 5)

    def __init__(self):
        Random_Npc._id_counter += 1
        self.id = Random_Npc._id_counter
        self.npc_level = Random_Npc.choose_level(self)
        self.npc_name = gen.generate_full_name(gen.first_name_elements, gen.last_name_elements)
        self.npc_race, self.npc_subrace = Random_Npc.choose_race(self)
        self.npc_class = Random_Npc.choose_class(self)
        self.npc_class_proficiencies = self.npc_class["proficiencies"]
        self.base_stats = self.set_base_stats()
        self.npc_hp = self.set_health_points()
        self.handling_level_ups()

        print(f"""Level: {self.npc_level}, HP: {self.npc_hp}, Name: {self.npc_name}, Class: {self.npc_class["name"]}
Race: {self.npc_race["name"]}, Subrace: {self.npc_subrace["name"]}, 
Main Stat: {self.npc_class["main_stat"]}, Saving Throws: {self.npc_class_proficiencies["saving_throws"]}, Starting HP: {self.npc_class["starting_hp"]}
Base Stats: {self.base_stats}""")
        
    def set_base_stats(self):
        base_stats = {"STR": 8, "DEX": 8, "CON": 8, "INT": 8, "WIS": 8, "CHA": 8}
        for stat in base_stats:
                if stat in self.npc_class_proficiencies["saving_throws"]:
                    base_stats[stat] += 2
        return base_stats
    
    def set_health_points(self):
        hp_stat_rolls = []
        base_hp = self.npc_class["starting_hp"]

        for i in range(1, self.npc_level):
            roll = random.randint(3, self.npc_class["starting_hp"])
            hp_stat_rolls.append(roll)
            base_hp += roll

        print(hp_stat_rolls)
        return base_hp
    
    def handling_level_ups(self):
        if self.npc_level > 3:
            self.base_stats[self.npc_class["main_stat"]] += 2

def create_random_npc(num):
     for i in range(num):
          Random_Npc()

create_random_npc(1)