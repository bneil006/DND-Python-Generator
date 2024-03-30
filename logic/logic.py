import time
from important_classes.npc import *

npc_dict = {
    "npc": {
    }
}

def create_npcs(number):
    total_npcs = 0

    while total_npcs < number:
        npc = Npc()
        if npc.name in npc_dict["npc"]:
            pass
        else:
            total_npcs += 1
            npc_dict["npc"][npc.name] = {
                "race": npc.npc_race_name,
                "subrace": npc.npc_race_instance.subrace,
                "class": npc.npc_class,
                "special_race_info": npc.special_info,
                "stat_block": npc.stat_block,
                "starting_pack": npc.starting_pack
            }

def print_npc_details():
    for npc_name, details in npc_dict["npc"].items():
        print(f"NPC Name: {npc_name}")
        print(f"Race: {details['race']}")
        print(f"Subrace: {details['subrace']}")
        print(f"Class: {details['class']}")
        print(f"Special Race Info: {details['special_race_info']}")
        print(f"Starting Pack: {details['starting_pack']}")
        print("Stat Block:")
        for stat, value in details['stat_block'].items():
            print(f"{stat}: {value}")
        print("\n")

def main():
    start_time = time.time()

    create_npcs(25)
    # print(npc_dict)

    print_npc_details()

    end_time = time.time()
    print(f"TIME: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()