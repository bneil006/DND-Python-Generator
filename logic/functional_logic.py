from important_classes.npc import *

persistant_npc_dict = {"npc": {}}

def add_npc_to_dict(npc, npc_dict):
    if npc.name not in npc_dict:
        npc_dict[npc.name] = {
            "id": npc.id,
            "race": npc.npc_race_name,
            "subrace": npc.npc_subrace,
            "class": npc.npc_class,
            "hp": npc.npc_hp,
            "level": npc.npc_level,
            "special_race_info": npc.special_info,
            "stat_block": npc.stat_block,
            "starting_pack": npc.starting_pack
        }
        return True
    return False

def create_npcs(number):
    used_names = set()
    attempts = 0
    max_attempts = 100

    while len(used_names) < number:
        npc = Npc()
        if npc.name not in used_names:
            add_npc_to_dict(npc, persistant_npc_dict["npc"])
            used_names.add(npc.name)
            attempts = 0
        else:
            attempts += 1
            if attempts > max_attempts:
                print("Reached a limit on generating unique names.")
                break

def create_npcs_temporary(number):
    npc_dict_temp = {"npc": {}}
    used_names = set()
    attempts = 0
    max_attempts = 100

    while len(used_names) < number:
        npc = Npc()
        if npc.name not in used_names:
            add_npc_to_dict(npc, npc_dict_temp["npc"])
            used_names.add(npc.name)
            attempts = 0
        else:
            attempts += 1
            if attempts > max_attempts:
                print("Reached a limit on generating unique names.")
                break

    return npc_dict_temp

def npc_names(npc_dict):
    names = []
    for name in npc_dict["npc"]:
        names.append(name)
    
    return names