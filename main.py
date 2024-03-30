import time
from npcs.npc import *
from functional_logic import *
from models import *
from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()

number = 1
npc_list = []

@app.get("/")
async def root():
    return {"message": f"Hello world"}

@app.get("/npcs_mass_entry")
async def get_npcs(number: int = Query(number, title="Number of NPCs", description="The number of NPCs to generate.")):
    create_npcs(number)
    return {"npcs": persistant_npc_dict}

@app.get("/npcs_temp")
async def get_npcs_temp(number: int = Query(number)):
    npc_dict_temp = create_npcs_temporary(number)
    return {"npcs_temp": npc_dict_temp}

@app.get("/npc_names")
async def get_npc_names():
    npc_na = npc_names()
    return {"npc_names": npc_na}

@app.get("/npcs_list")
async def get_npcs():
    return {"npcs": npc_list}

@app.get("/npcs/{npc_id}")
async def get_npcs(npc_id: int):
    for npc_name, npc_details in persistant_npc_dict["npc"].items():
        if npc_details['id'] == npc_id:
            return {"npc": npc_details}
    
    return {"message": "NPC not found"}

@app.post("/npcs_list")
async def create_npc(npc_item: Npc_item):
    npc_list.append(npc_item)
    return {"npc_item": "Npc has been added"}