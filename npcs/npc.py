import random
from name_dict import *
from equipment import *

class Npc():
    _id_counter = 0

    def __init__(self):
        Npc._id_counter +=1
        self.id = Npc._id_counter
        self.first_name = random.choice(list(F_NAMES_DICT.values()))
        self.last_name = random.choice(list(L_NAMES_DICT.values()))
        self.name = f"{self.first_name} {self.last_name}"
        self.npc_class = random.choice(list(NPC_CLASS_DICT.values()))
        chosen_race = random.choice(list(NPC_RACE_DICT.values()))
        self.npc_race_name = chosen_race[0]
        self.npc_race_instance = chosen_race[1]
        self.special_info = self.npc_race_instance.class_race_info()
        self.stat_block = self.npc_race_instance.base_stat_modifiers()
        self.starting_pack = random.choice(list(STARTING_EQUIPMENT_PACKS.items()))

class Races():
    def __init__(self):
        self.BASE_STATS = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }
        self.subrace_dict = {}
        self.subrace = None

    def class_race_info(self):
        return "Generic class race information"
    
    def subrace_picker(self):
        if self.subrace_dict:
            self.subrace = random.choice(list(self.subrace_dict.values()))
        else:
            self.subrace = "None"
        return self.subrace
    
    def base_stat_modifiers(self):
        return self.BASE_STATS

class Dwarf(Races):
    def __init__(self):
        super().__init__()
        self.subrace_dict = {
            1: "Hill Dwarf",
            2: "Mountain Dwarf"
        }
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Stout, skilled in craft and combat, with a strong sense of kinship and tradition."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["CON"] += 2
        if self.subrace == "Hill Dwarf":
            modified_stats["WIS"] += 1
        else:
            modified_stats["STR"] += 2
        return modified_stats

class Elf(Races):
    def __init__(self):
        super().__init__()
        self.subrace_dict = {
            1: "High Elf",
            2: "Wood Elf",
            3: "Dark Elf"
        }
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Ancient, magical, and graceful, with a deep bond to nature and art."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["DEX"] += 2
        if self.subrace == "High Elf":
            modified_stats["INT"] += 1
        elif self.subrace == "Wood Elf":
            modified_stats["WIS"] += 1
        else:
            modified_stats["CHA"] += 1
        return modified_stats

class Halfling(Races):
    def __init__(self):
        super().__init__()
        self.subrace_dict = {
            1: "Lightfoot Halfling",
            2: "Stout Halfling"
        }
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Cheerful and resourceful small folk who cherish community and comfort."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["DEX"] += 2
        if self.subrace == "Lightfoot Halfling":
            modified_stats["CHA"] += 1
        else:
            modified_stats["CON"] += 1
        return modified_stats

class Human(Races):
    def __init__(self):
        super().__init__()
        self.subrace = None
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Remarkably diverse and ambitious, thriving on innovation and exploration."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["STR"] += 1
        modified_stats["DEX"] += 1
        modified_stats["CON"] += 1
        modified_stats["INT"] += 1
        modified_stats["WIS"] += 1
        modified_stats["CHA"] += 1
        return modified_stats

class Dragonborn(Races):
    def __init__(self):
        super().__init__()
        self.subrace = None
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Proud, dragon-blooded warriors with a natural command of power and respect."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["STR"] += 2
        modified_stats["CHA"] += 1
        return modified_stats

class Gnome(Races):
    def __init__(self):
        super().__init__()
        self.subrace_dict = {
            1: "Forest Gnome",
            2: "Rock Gnome"
        }
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Inventive and curious, blending mischief with a keen intellect."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["INT"] += 2
        if self.subrace == "Forest Gnome":
            modified_stats["DEX"] += 1
        else:
            modified_stats["CON"] += 1
        return modified_stats

class Half_elf(Races):
    def __init__(self):
        super().__init__()
        self.subrace = None
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Versatile and charismatic, bridging the gap between human and elven worlds."
    
    def base_stat_modifiers(self):
        additional_modified_stats = self.BASE_STATS.copy()
        del additional_modified_stats["CHA"]

        modified_stats = self.BASE_STATS.copy()
        modified_stats["CHA"] += 2

        for i in range(0, 2):
            random_stat_selection = random.choice(list(additional_modified_stats))
            modified_stats[random_stat_selection] += 1

        return modified_stats

class Half_orc(Races):
    def __init__(self):
        super().__init__()
        self.subrace = None
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Strong and tenacious, often battling against prejudice with fierce loyalty."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["STR"] += 2
        modified_stats["CON"] += 1
        return modified_stats

class Tiefling(Races):
    def __init__(self):
        super().__init__()
        self.subrace = None
        self.subrace = self.subrace_picker()
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Mystical and misunderstood, bearing the mark of their infernal heritage with defiance."
    
    def base_stat_modifiers(self):
        modified_stats = self.BASE_STATS.copy()
        modified_stats["INT"] += 1
        modified_stats["CHA"] += 2
        return modified_stats

NPC_RACE_DICT = {
    1: ["Dwarf", Dwarf()],
    2: ["Elf", Elf()],
    3: ["Halfling", Halfling()],
    4: ["Human", Human()],
    5: ["Dragonborn", Dragonborn()],
    6: ["Gnome", Gnome()],
    7: ["Half Elf", Half_elf()],
    8: ["Half Orc", Half_orc()],
    9: ["Tiefling", Tiefling()]
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