#### USING THIS FILE JUST FOR TESTING PURPOSES


import random

def choose_random_item(dictionary):
    return random.choice(list(dictionary.values()))

class Races():
    def __init__(self):
        self.BASE_STATS = {
            "STR": 8,
            "DEX": 8,
            "CON": 8,
            "INT": 8,
            "WIS": 8,
            "CHA": 8
        }
        self.subrace_dict = {}
        self.subrace = None
        self.base_stat_modifiers()

    def class_race_info(self):
        return "Generic class race information"
    
    def subrace_picker(self):
        if self.subrace_dict:
            self.subrace = random.choice(list(self.subrace_dict.values()))
        else:
            self.subrace = "None"
        return self.subrace
    
    def base_stat_modifiers(self):
        point_buy = 27

        while point_buy > 0:
            stat_modifier = random.choice(list(self.BASE_STATS))
            stat_level = self.BASE_STATS[stat_modifier]
            if stat_level >= 13 and point_buy >= 2:
                point_buy -= 2
                self.BASE_STATS[stat_modifier] += 1
            elif stat_level >= 12 and point_buy >= 1:
                point_buy -= 1
                self.BASE_STATS[stat_modifier] += 1
            elif stat_level < 13 and point_buy >= 2:
                point_buy -= 2
                self.BASE_STATS[stat_modifier] += 2
            elif stat_level <= 12 and point_buy >= 1:
                point_buy -= 1
                self.BASE_STATS[stat_modifier] += 1
            else:
                print("Base stat point buy Error")
    
race = Races()

for key, item in race.BASE_STATS.items():
    print(key, item)

print(race.BASE_STATS)