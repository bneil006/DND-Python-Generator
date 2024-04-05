from test2 import *

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
            "bonus_stats": npc.bonus_stats,
            "equipment_pack": npc.equipment_pack
        }
        return True
    return False