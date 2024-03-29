NPC_RACE_DICT = {
    1: "Dwarf",
    2: "Elf",
    3: "Halfling",
    4: "Human",
    5: "Dragonborn",
    6: "Gnome",
    7: "Half Elf",
    8: "Half Orc",
    9: "Tiefling"
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

F_NAMES_DICT = {
    1: "Cheal",
    2: "Elkin",
    3: "Goff",
    4: "Knepel",
    5: "Adair",
    6: "Vander"
}

L_NAMES_DICT = {
    1: "Esha",
    2: "Fazal",
    3: "Goggin",
    4: "Golin",
    5: "Vanderthrump",
    6: "Wind"
}

class Npc():
    def __init__(self, first_name, last_name, npc_race, npc_class):
        self.first_name = F_NAMES_DICT[first_name]
        self.last_name = L_NAMES_DICT[last_name]
        self.name = self.first_name + " " + self.last_name
        self.npc_race = NPC_RACE_DICT[npc_race]
        self.npc_class = NPC_CLASS_DICT[npc_class]
    
    def get_npc_info(self):
        print(f"NAME: {self.name}, RACE: {self.npc_race}, CLASS: {self.npc_class}")

class Races():
    def class_race_info():
        print("Generic class race information")

class Dwarf(Races):
    def class_race_info():
        print("Dwarfs are hearty characters")

class Elf(Races):
    def class_race_info():
        print("Elfs are agile creatures")

class Halfling(Races):
    pass

class Human(Races):
    pass

class Dragonborn(Races):
    pass

class Gnome(Races):
    pass

class Half_Elf(Races):
    pass

class Half_Orc(Races):
    pass

class Tiefling(Races):
    pass