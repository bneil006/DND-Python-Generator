import endpoint_dicts.races as races
import endpoint_dicts.classes as classes
import endpoint_dicts.npc_specifics as specifics
import important_classes.equipment as equipment
import important_classes.generators as gen
import random

def choose_pack(stat, pack):
    return pack[stat]

class RandomNPC():
    _id_counter = 0

    @staticmethod
    def choose_race():
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
    
    @staticmethod
    def choose_class():
         return random.choice(classes.CLASS_DICT["results"])
    
    @staticmethod
    def choose_level():
          return random.randint(1, 5)

    def __init__(self):
        RandomNPC._id_counter += 1
        self.id = RandomNPC._id_counter
        self.npc_level = RandomNPC.choose_level()
        self.npc_name = gen.generate_full_name(gen.first_name_elements, gen.last_name_elements)
        self.npc_race, self.npc_subrace = RandomNPC.choose_race()
        self.npc_class = RandomNPC.choose_class()
        self.npc_class_proficiencies = self.npc_class["proficiencies"]
        self.base_stats = self.set_base_stats()
        self.npc_hp, self.npc_hp_rolled = self.set_health_points()
        self.npc_main_weapon, self.npc_secondary_weapon, self.npc_armor, self.npc_trinket, self.npc_other_item = self.set_npc_items()

    def npc_information(self):
        print(f"""Hp Increase: {self.npc_hp_rolled}
Level: {self.npc_level}, HP: {self.npc_hp}, Name: {self.npc_name}, Class: {self.npc_class["name"]}
Race: {self.npc_race["name"]}, Subrace: {self.npc_subrace["name"]}, 
Main Stat: {self.npc_class["main_stat"]}, Saving Throws: {self.npc_class_proficiencies["saving_throws"]}, Starting HP: {self.npc_class["starting_hp"]}
Base Stats: {self.base_stats}""")
        
    def set_base_stats(self):
        total_points_remaining = 27
        stat_cost = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9, 16: 11, 17: 13, 18: 15, 19: 17, 20: 19}
        base_stats = {"STR": 8, "DEX": 8, "CON": 8, "INT": 8, "WIS": 8, "CHA": 8}
        
        # bard and paladin have different main stats than their saving throws so adding in +2 initially to their specific classes base_stats
        if self.npc_class["index"] == "bard" or self.npc_class["index"] == "paladin":
            base_stats[self.npc_class["main_stat"]] += 2

        # adding +2 to base_stats based on the classes saving_throws
        for stat in base_stats:
            if stat in self.npc_class_proficiencies["saving_throws"]:
                base_stats[stat] += 2

        # subtracting points spent from the total point buy of 27 points based on dnd 5e rules
        for stat, points in base_stats.items():
            total_points_remaining -= stat_cost[points]
        
        # spending all the rest of the stat points remaining randomly
        while total_points_remaining > 0:
            choice = random.choice(list(base_stats))
            if base_stats[choice] >= 15:
                continue
            else:
                if base_stats[choice] >= 13 and total_points_remaining >= 2:
                    base_stats[choice] += 1
                    total_points_remaining -= 2
                elif base_stats[choice] <= 12 and total_points_remaining >= 1:
                    base_stats[choice] += 1
                    total_points_remaining -= 1

        # adding in +2 points to the main stat for the level advancement at level 4 to each class and after the initial point buy
        if self.npc_level > 3:
            base_stats[self.npc_class["main_stat"]] += 2

        # adding in racial and subracial bonuses now after initial point buy and advancements
        for stat, points in base_stats.items():
            if stat in self.npc_race["ability_score_increases"]:
                base_stats[stat] += self.npc_race["ability_score_increases"][stat]

            # only runs if subrace is present and not None or []
            if self.npc_race["subraces"]:
                if stat in self.npc_subrace["ability_score_increases"]:
                    base_stats[stat] += self.npc_subrace["ability_score_increases"][stat]

        return base_stats
    
    def set_health_points(self):
        hp_stat_rolls = []
        base_hp = self.npc_class["starting_hp"]

        for i in range(1, self.npc_level):
            roll = random.randint(3, self.npc_class["starting_hp"])
            hp_stat_rolls.append(roll)
            base_hp += roll

        return base_hp, hp_stat_rolls
    
    def set_npc_items(self):
        equipment_selection = choose_pack(self.npc_class["main_stat"], equipment.NPC_PACKS)

        weapon = random.choice(list(equipment_selection["main_weapon"]))
        secondary_weapon = random.choice(list(equipment_selection["secondary_weapon"]))
        armor = random.choice(list(equipment_selection["chest"]))
        trinket = random.choice(list(equipment_selection["trinket"]))
        other_item = random.choice(list(equipment_selection["other"]))
        return weapon, secondary_weapon, armor, trinket, other_item

def create_random_npc_temp_dict(num):
    npc_dict_temp = {"npcs": []}
    for i in range(num):
        npc = RandomNPC()
        npc_details = {
            "id": npc.id,
            "name": npc.npc_name,
            "race": npc.npc_race["name"],
            "subrace": npc.npc_subrace["name"],
            "class": npc.npc_class["name"],
            "hp": npc.npc_hp,
            "level": npc.npc_level,
            "stat_block": npc.base_stats,
            "main_stat": npc.npc_class["main_stat"],
            "saving_throws": npc.npc_class_proficiencies["saving_throws"],
            "main_weapon": npc.npc_main_weapon,
            "secondary_weapon": npc.npc_secondary_weapon,
            "armor": npc.npc_armor,
            "trinket": npc.npc_trinket,
            "other_item": npc.npc_other_item
        }
        npc_dict_temp["npcs"].append(npc_details)
    return npc_dict_temp

print(create_random_npc_temp_dict(1))