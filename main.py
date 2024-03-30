from fastapi import FastAPI, Query
import time
from npcs.npc import *

app = FastAPI()

npc_dict = {
    "npc": {
    }
}

name = "Haley"
number = 1

@app.get("/")
async def root():
    return {"message": f"Hello {name}"}

@app.get("/npcs")
async def get_npcs(number: int = Query(number, title="Number of NPCs", description="The number of NPCs to generate.")):
    start_time = time.time()

    create_npcs(number)
    print_npc_details()

    end_time = time.time()
    print(f"TIME: {end_time - start_time} seconds")
    return {"npcs": npc_dict}

@app.get("/npcs_temp")
async def get_npcs_temp(number: int = Query(number)):
    npc_dict_temp = create_npcs_temporary(number)
    print(f"PRINT STATEMENT: {npc_dict_temp}")

    return {"npcs_temp": npc_dict_temp}

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