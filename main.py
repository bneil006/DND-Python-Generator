import time
from npcs.npc import *

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
                "class": npc.npc_class,
                "special_race_info": npc.special_info,
                "stat_block": npc.stat_block
            }

def main():
    start_time = time.time()

    create_npcs(15)
    print(npc_dict)

    end_time = time.time()
    print(f"TIME: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()