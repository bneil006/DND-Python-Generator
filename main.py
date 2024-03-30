import time
from npcs.npc import *
from functional_logic import *
from models import *
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Dict, List, Union


app = FastAPI()

number = 1
npc_list = []

# root, just adding this comment because I bearly know anything about
# FastAPI and need to really dig into every thing
@app.get("/")
async def root():
    return {"message": f"Hello world"}

# pretty simple, searches for an id
@app.get("/npcs/{npc_id}")
async def get_npc(npc_id: int):
    for npc_name, npc_details in persistant_npc_dict["npc"].items():
        if npc_details['id'] == npc_id:
            return {"npc_name": npc_name, "npc": npc_details}
    
    return {"message": "NPC not found"}

# Can delete now but something about FastAPI is confusing..
# Need more practic.. look at this function again
@app.delete("/npcs/{npc_id}")
async def delete_npc(npc_id: int):
    npc_name_to_delete = None
    for npc_name, npc_details in persistant_npc_dict["npc"].items():
        if npc_details['id'] == npc_id:
            npc_name_to_delete = npc_name
            break
    
    if npc_name_to_delete:
        del persistant_npc_dict["npc"][npc_name_to_delete]
        return {"message": "NPC has been deleted"}
    
    return {"message": "NPC not found"}

# Post method but got a little lost in the sauce, need to come back to Pydantic
# and really make sure I know what I'm doing here..
@app.post("/npcs")
async def create_npc(npc_item: Npc_item):
    for npc_details in persistant_npc_dict["npc"].values():
        if npc_details['id'] == npc_item.id:
            raise Exception("id already exists")

    # Convert the Pydantic model to a dictionary and add it to persistant_npc_dict
    npc_dict = npc_item.dict()
    persistant_npc_dict["npc"][npc_item.name] = npc_dict

    return {"message": "NPC has been added", "npc_item": npc_dict}

# Added a way to call a function in my functional_logic that generate a # of
# Randomly created npcs and then get's them here, the data persists in the dict
# atleast until the server restarts / shuts down - can add to a database later
# if I can figure that out..
@app.get("/npcs_mass_entry")
async def get_npcs(number: int = Query(number, title="Number of NPCs", description="The number of NPCs to generate.")):
    create_npcs(number)
    return {"npcs": persistant_npc_dict}

# Calling a function to generate a # of Randomly created npcs and then get them here
# the data doesn't persist and makes a new temporary dictionary every single time we
# refresh the page / run the create_npcs_temporary(number) function
@app.get("/npcs_temp")
async def get_npcs_temp(number: int = Query(number)):
    npc_dict_temp = create_npcs_temporary(number)
    return {"npcs_temp": npc_dict_temp}

# using a url and GET to pullback all the names in the persistant dict
# this is mostly for testing
@app.get("/npc_names")
async def get_npc_names():
    npc_na = npc_names()
    return {"npc_names": npc_na}