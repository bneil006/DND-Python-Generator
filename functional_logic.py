from npcs.npc import *

persistant_npc_dict = {
    "npc": {
    }
}

def create_npcs(number):
    total_npcs = 0

    while total_npcs < number:
        npc = Npc()
        if npc.name in persistant_npc_dict["npc"]:
            pass
        else:
            total_npcs += 1
            persistant_npc_dict["npc"][npc.name] = {
                "id": npc.id,
                "race": npc.npc_race_name,
                "subrace": npc.npc_race_instance.subrace,
                "class": npc.npc_class,
                "special_race_info": npc.special_info,
                "stat_block": npc.stat_block,
                "starting_pack": npc.starting_pack
            }

def create_npcs_temporary(number):
    total_npcs = 0
    npc_dict_temp = {
        "npc": {
        }
    }

    while total_npcs < number:
        npc = Npc()
        if npc.name in npc_dict_temp["npc"]:
            pass
        else:
            total_npcs += 1
            npc_dict_temp["npc"][npc.name] = {
                "race": npc.npc_race_name,
                "subrace": npc.npc_race_instance.subrace,
                "class": npc.npc_class,
                "special_race_info": npc.special_info,
                "stat_block": npc.stat_block,
                "starting_pack": npc.starting_pack
            }
    
    return npc_dict_temp

def npc_names():
    names = []
    for name in persistant_npc_dict["npc"]:
        names.append(name)
    
    return names