import random
import important_classes.equipment as equipment
import important_classes.generators as gen

def choose_random_item(dictionary):
    return random.choice(list(dictionary.values()))

def choose_pack(stat, pack):
            return pack[stat]

class Npc():
    _id_counter = 0

    def __init__(self):
        Npc._id_counter += 1
        self.id = Npc._id_counter
        self.first_name = gen.generate_name(gen.first_name_elements)
        self.last_name = gen.generate_name(gen.last_name_elements)
        self.name = f"{self.first_name} {self.last_name}"
        self.npc_class = choose_random_item(NPC_CLASS_DICT)
        chosen_race = choose_random_item(NPC_RACE_DICT)
        chosen_race_name, chosen_race_class = choose_random_item(NPC_RACE_DICT)
        self.npc_race_instance = chosen_race_class()  # Instantiate the race class here
        self.npc_race_name = chosen_race_name
        self.npc_subrace = self.npc_race_instance.subrace
        self.special_info = self.npc_race_instance.class_race_info()
        self.stat_block = self.npc_race_instance.BASE_STATS.copy()
        self.highest_stat = self.npc_race_instance.highest_modifier()
        self.npc_hp = 8
        self.npc_level = 1

        self.main_weapon = equipment.choose_main_weapon(self.highest_stat)
        self.secondary_weapon = equipment.choose_secondary_weapon(self.highest_stat)
        self.chest = equipment.choose_chest(self.highest_stat)
        self.trinket = equipment.choose_trinket(self.highest_stat)
        self.other = equipment.choose_other(self.highest_stat)

        ### CHOOSING GEAR ###
        self.EQUIPMENT_PACKS = {
            "STR": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
                ],
            "DEX": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
                ],
            "CON": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
            ],
            "INT": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
            ],
            "WIS": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
            ],
            "CHA": [
                self.main_weapon,
                self.secondary_weapon,
                self.chest,
                self.trinket,
                self.other
            ],
        }

        self.equipment_pack = choose_pack(self.highest_stat, self.EQUIPMENT_PACKS)
        self.bonus_stats = self.npc_race_instance.bonus_stats
        print(self.bonus_stats)


class Races():
    def __init__(self):
        self.BASE_STATS = {"STR": 8, "DEX": 8, "CON": 8, "INT": 8, "WIS": 8, "CHA": 8}
        self.bonus_stats = {"details": []}
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Generic class race information"

    def base_stat_modifiers(self):
        point_buy = 27
        cost_table = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        stats_keys = list(self.BASE_STATS.keys())
        
        while point_buy > 0:
            random.shuffle(stats_keys)
            for stat_modifier in stats_keys:
                stat_level = self.BASE_STATS[stat_modifier]
                if stat_level < 15:
                    next_cost = cost_table.get(stat_level + 1, float('inf')) - cost_table.get(stat_level, 0)
                    if point_buy >= next_cost:
                        self.BASE_STATS[stat_modifier] += 1
                        point_buy -= next_cost
                        break
    
    def highest_modifier(self):
        current_highest = 0
        highest_stat = ""
        for a, b in self.BASE_STATS.items():
            if b > current_highest:
                current_highest = b
                highest_stat = a
        
        return highest_stat

class Dwarf(Races):
    def __init__(self):
        self.subrace_dict = {1: "Hill Dwarf", 2: "Mountain Dwarf"}
        self.subrace = random.choice(list(self.subrace_dict.values()))
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Stout, skilled in craft and combat, with a strong sense of kinship and tradition."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["CON"] += 2
        self.bonus_stats["details"].append({
            "name": "Dwarf Racial Bonus",
            "stat_name": "CON",
            "bonus_amount": 2
        })

        if self.subrace == "Hill Dwarf":
            self.BASE_STATS["WIS"] += 1
            self.bonus_stats["details"].append({
            "name": "Hill Dwarf Subracial Bonus",
            "stat_name": "WIS",
            "bonus_amount": 1
        })
        elif self.subrace == "Mountain Dwarf":
            self.BASE_STATS["STR"] += 2
            self.bonus_stats["details"].append({
            "name": "Mountain Dwarf Subracial Bonus",
            "stat_name": "STR",
            "bonus_amount": 2
        })

class Elf(Races):
    def __init__(self):
        self.subrace_dict = {1: "High Elf", 2: "Wood Elf", 3: "Dark Elf"}
        self.subrace = random.choice(list(self.subrace_dict.values()))
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Ancient, magical, and graceful, with a deep bond to nature and art."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["DEX"] += 2
        self.bonus_stats["details"].append({
            "name": "Elf Racial Bonus",
            "stat_name": "DEX",
            "bonus_amount": 2
        })
        if self.subrace == "High Elf":
            self.BASE_STATS["INT"] += 1
            self.bonus_stats["details"].append({
            "name": "High Elf subracial Bonus",
            "stat_name": "INT",
            "bonus_amount": 1
        })
        elif self.subrace == "Wood Elf":
            self.BASE_STATS["WIS"] += 1
            self.bonus_stats["details"].append({
            "name": "Wood Elf subracial Bonus",
            "stat_name": "WIS",
            "bonus_amount": 1
        })
        else:
            self.BASE_STATS["CHA"] += 1
            self.bonus_stats["details"].append({
            "name": "Dark Elf subracial Bonus",
            "stat_name": "CHA",
            "bonus_amount": 1
        })

class Halfling(Races):
    def __init__(self):
        self.subrace_dict = {1: "Lightfoot Halfling", 2: "Stout Halfling"}
        self.subrace = random.choice(list(self.subrace_dict.values()))
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Cheerful and resourceful small folk who cherish community and comfort."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["DEX"] += 2
        if self.subrace == "Lightfoot Halfling":
            self.BASE_STATS["CHA"] += 1
        else:
            self.BASE_STATS["CON"] += 1

class Human(Races):
    def __init__(self):
        self.subrace = None
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Remarkably diverse and ambitious, thriving on innovation and exploration."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["STR"] += 1
        self.BASE_STATS["DEX"] += 1
        self.BASE_STATS["CON"] += 1
        self.BASE_STATS["INT"] += 1
        self.BASE_STATS["WIS"] += 1
        self.BASE_STATS["CHA"] += 1

class Dragonborn(Races):
    def __init__(self):
        self.subrace = None
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Proud, dragon-blooded warriors with a natural command of power and respect."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["STR"] += 2
        self.BASE_STATS["CHA"] += 1

class Gnome(Races):
    def __init__(self):
        self.subrace_dict = {1: "Forest Gnome", 2: "Rock Gnome"}
        self.subrace = random.choice(list(self.subrace_dict.values()))
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Inventive and curious, blending mischief with a keen intellect."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["INT"] += 2
        if self.subrace == "Forest Gnome":
            self.BASE_STATS["DEX"] += 1
        else:
            self.BASE_STATS["CON"] += 1

class Half_elf(Races):
    def __init__(self):
        self.subrace = None
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Versatile and charismatic, bridging the gap between human and elven worlds."
    
    def subrace_stat_modifiers(self):
        additional_modified_stats = self.BASE_STATS.copy()
        del additional_modified_stats["CHA"]

        self.BASE_STATS["CHA"] += 2

        for i in range(0, 2):
            random_stat_selection = random.choice(list(additional_modified_stats))
            self.BASE_STATS[random_stat_selection] += 1

class Half_orc(Races):
    def __init__(self):
        self.subrace = None
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Strong and tenacious, often battling against prejudice with fierce loyalty."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["STR"] += 2
        self.BASE_STATS["CON"] += 1

class Tiefling(Races):
    def __init__(self):
        self.subrace = None
        super().__init__()
        self.subrace_stat_modifiers()

    def class_race_info(self):
        return "Mystical and misunderstood, bearing the mark of their infernal heritage with defiance."
    
    def subrace_stat_modifiers(self):
        self.BASE_STATS["INT"] += 1
        self.BASE_STATS["CHA"] += 2

NPC_RACE_DICT = {
    1: ["Dwarf", Dwarf],
    2: ["Elf", Elf],
    3: ["Halfling", Halfling],
    4: ["Human", Human],
    5: ["Dragonborn", Dragonborn],
    6: ["Gnome", Gnome],
    7: ["Half Elf", Half_elf],
    8: ["Half Orc", Half_orc],
    9: ["Tiefling", Tiefling]
}

NPC_CLASS_DICT = {
    1: "Barbarian",
    2: "Bard",
    3: "Cleric",
    4: "Druid",
    5: "Fighter",
    6: "Monk",
    7: "Paladin",
    8: "Ranger",
    9: "Rogue",
    10: "Sorcerer",
    11: "Warlock",
    12: "Wizard"
}