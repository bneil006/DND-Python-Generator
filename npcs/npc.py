import random
from name_dict import *

class Npc():
    def __init__(self):
        self.first_name = random.choice(list(F_NAMES_DICT.values()))
        self.last_name = random.choice(list(L_NAMES_DICT.values()))
        self.name = f"{self.first_name} {self.last_name}"
        self.npc_class = random.choice(list(NPC_CLASS_DICT.values()))
        chosen_race = random.choice(list(NPC_RACE_DICT.values()))
        self.npc_race_name = chosen_race[0]
        self.npc_race_instance = chosen_race[1]
        self.special_info = self.npc_race_instance.class_race_info()

class Races():
    def class_race_info(self):
        return "Generic class race information"

class Dwarf(Races):
    def class_race_info(self):
        return "Stout, skilled in craft and combat, with a strong sense of kinship and tradition."

class Elf(Races):
    def class_race_info(self):
        return "Ancient, magical, and graceful, with a deep bond to nature and art."

class Halfling(Races):
    def class_race_info(self):
        return "Cheerful and resourceful small folk who cherish community and comfort."

class Human(Races):
    def class_race_info(self):
        return "Remarkably diverse and ambitious, thriving on innovation and exploration."

class Dragonborn(Races):
    def class_race_info(self):
        return "Proud, dragon-blooded warriors with a natural command of power and respect."

class Gnome(Races):
    def class_race_info(self):
        return "Inventive and curious, blending mischief with a keen intellect."

class Half_elf(Races):
    def class_race_info(self):
        return "Versatile and charismatic, bridging the gap between human and elven worlds."

class Half_orc(Races):
    def class_race_info(self):
        return "Strong and tenacious, often battling against prejudice with fierce loyalty."

class Tiefling(Races):
    def class_race_info(self):
        return "Mystical and misunderstood, bearing the mark of their infernal heritage with defiance."

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