import random
from npcs.npc import *

npc_dict = {
    "npc": {}
}

def create_npcs(number):
    count = 0

    while count < number:
        count += 1
        npc_first_name = random.randint(1, len(F_NAMES_DICT))
        npc_last_name = random.randint(1, len(L_NAMES_DICT))
        npc_race = random.randint(1, len(NPC_RACE_DICT))
        npc_class = random.randint(1, len(NPC_CLASS_DICT))

        npc = Npc(npc_first_name, npc_last_name, npc_race, npc_class)
        if npc.name in npc_dict["npc"]:
            print(f"SKIPPING {npc.name} ALREADY EXISTS!")
        else:
            npc_dict["npc"][npc.name] = {
                "race": npc.npc_race,
                "class": npc.npc_class
            }

def main():
    number = int(input("How many NPCS: "))
    create_npcs(number)
    print(npc_dict)
    

if __name__ == '__main__':
    main()