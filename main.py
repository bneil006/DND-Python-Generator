import random
from npcs.npc import *

npc_dict = {}

def create_npc():
    npc_first_name = random.randint(1, len(F_NAMES_DICT))
    npc_last_name = random.randint(1, len(L_NAMES_DICT))
    npc_race = random.randint(1, len(NPC_RACE_DICT))
    npc_class = random.randint(1, len(NPC_CLASS_DICT))

    return Npc(npc_first_name, npc_last_name, npc_race, npc_class)

def create_muli_npc(number):
    npc_list = []

    for i in range(0, number):
        npc_list.append(create_npc().get_npc_info())
    return npc_list

def main():
    number = int(input("How many NPCS: "))
    x = create_muli_npc(number)
    

if __name__ == '__main__':
    main()