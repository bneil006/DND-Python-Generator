import endpoint_dicts.races as races

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

race = "dwarf"
subrace = "mountain-dwarf"
race_info, subrace_info = parse_races_dict(race, subrace)

print(race_info["tool_proficiencies"])
