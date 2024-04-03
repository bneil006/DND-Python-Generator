import endpoint_dicts.races as races
import random

class Npc():
    _id_counter = 0

    def __init__(self):
        Npc._id_counter += 1
        self.id = Npc._id_counter

def parse_races_dict(race_name, subrace_name):
    race_info = None  # Placeholder for race information
    subrace_info = None  # Placeholder for subrace information
    
    for race in races.RACE_DICT["results"]:
        if race["index"] == race_name:
            race_info = {
                "index": race["index"],
                "name": race["name"],
                "ability_score_increases": race["ability_score_increases"],
                "age": race["age"],
                "alignment": race["alignment"],
                "size": race["size"],
                "speed": race["speed"],
                "languages": race["languages"],
                "vision": race["vision"],
                "skill_proficiencies": race["skill_proficiencies"],
                "tool_proficiencies": race["tool_proficiencies"],
                "weapon_proficiencies": race["weapon_proficiencies"],
                "special_abilities": race["special_abilities"],
                "physical_description": race["physical_description"],
                "traits": race["traits"]
            }
            
            for subrace in race.get("subraces", []):
                if subrace["index"] == subrace_name:
                    subrace_info = {
                        "index": subrace["index"],
                        "name": subrace["name"],
                        "ability_score_increases": subrace["ability_score_increases"],
                        "skill_proficiencies": subrace.get("skill_proficiencies", []),
                        "traits": subrace["traits"]
                    }
                    break  # Stop searching once the subrace is found
            
            break  # Stop searching once the race is found
    
    return race_info, subrace_info

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

def get_race_instance(race_name, subrace_name=None):
    race_info, subrace_info = parse_races_dict(race_name, subrace_name)
    if race_info is not None:
        return Race(race_info, subrace_info)
    else:
        raise ValueError("Race not found")
