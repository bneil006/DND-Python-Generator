import important_classes.npc as npc

class Equipement():
    def __init__(self):
        # self.pack = npc
        pass

EQUIPMENT_PACKS = {
    "STR": [
        "Greatsword or Battleaxe",
        "Chain Mail",
        "Iron Gauntlets"
    ],
    "DEX": [
        "Rapier or Shortbow",
        "Leather Armor",
        "Thieves' Tools"
    ],
    "CON": [
        "Warhammer",
        "Scale Mail",
        "Shield"
    ],
    "INT": [
        "Quarterstaff",
        "Robes",
        "Spellbook"
    ],
    "WIS": [
        "Mace",
        "Padded Armor",
        "Holy Symbol"
    ],
    "CHA": [
        "Longsword",
        "Fine Clothes",
        "Musical Instrument (e.g., Lute, Flute)"
    ],
}

EQUIPMENT_PACK_SCHEMES = {
    "STR": {
        "Armor": {
            "Helm": [],
            "Chest": [],
            "Bracers": [],
            "Leggings": [],
            "Shoes": [],
            "Cape": []
        },
        "Weapons": {
            "Main Hand": [],
            "Off Hand": [],
            "Ranged": []
        },
        "Trinkets": [],
        "Other": []
        },
}

def choose_pack(stat):
    return EQUIPMENT_PACKS[stat]