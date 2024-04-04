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
        self.race, self.subrace = Random_Npc.choose_race(self)
        self.npc_class = Random_Npc.choose_class(self)
        print(f"ID: {self.id}, Name: {self.name}, Race: {self.race["name"]}, Subrace: {self.subrace["name"]}, Class: {self.npc_class["name"]}")

class Race:
    BASE_STATS = {"STR": 8, "DEX": 8, "CON": 8, "INT": 8, "WIS": 8, "CHA": 8}

    def __init__(self, race_info, subrace_info=None):
        self.race_info = race_info
        self.subrace_info = subrace_info
        self.stats = Race.BASE_STATS.copy()
        self.bonus_stats = {"details": []}
        self.base_stat_modifiers()

    def class_race_info(self):
        return f"Race: {self.race_info['name']}, Subrace: {self.subrace_info['name'] if self.subrace_info else 'None'}"

    def base_stat_modifiers(self):
        point_buy = 27
        cost_table = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        
        while point_buy > 0:
            stats_keys = list(self.stats.keys())
            random.shuffle(stats_keys)
            for stat_modifier in stats_keys:
                stat_level = self.stats[stat_modifier]
                if stat_level < 15:
                    next_cost = cost_table.get(stat_level + 1, float('inf')) - cost_table.get(stat_level, 0)
                    if point_buy >= next_cost:
                        self.stats[stat_modifier] += 1
                        point_buy -= next_cost
                        break

    def highest_modifier(self):
        highest_stat = max(self.stats, key=self.stats.get)
        return highest_stat, self.stats[highest_stat]

def create_random_npc(num):
     for i in range(num):
          Random_Npc()

create_random_npc(5)