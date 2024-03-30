from fastapi import FastAPI, Query
from important_classes.npc import *
from logic.functional_logic import *
from models import *
import time

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello world"}

@app.get("/npcs/{npc_id}")
async def get_npc(npc_id: int):
    for npc_name, npc_details in persistant_npc_dict["npc"].items():
        if npc_details['id'] == npc_id:
            return {"npc_name": npc_name, "npc": npc_details}
    
    return {"message": "NPC not found"}

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

@app.post("/npcs")
async def create_npc(npc_item: Npc_item):
    for npc_details in persistant_npc_dict["npc"].values():
        if npc_details['id'] == npc_item.id:
            raise Exception("id already exists")

    # Convert the Pydantic model to a dictionary and add it to persistant_npc_dict
    npc_dict = npc_item.dict()
    persistant_npc_dict["npc"][npc_item.name] = npc_dict

    return {"message": "NPC has been added", "npc_item": npc_dict}

@app.get("/npcs_generator_semi_persist")
async def get_npcs(number: int = Query(default=5, le=500)):
    start = time.time()
    create_npcs(number)
    end = time.time()
    print(f"Operation took {end - start} seconds")
    # Return your persistent NPC dictionary here
    return {"npcs": persistant_npc_dict}

@app.get("/npcs_generator_temp")
async def get_npcs_temp(number: int = Query(default=5, le=500)):
    start = time.time()

    npc_dict_temp = create_npcs_temporary(number)
    
    end = time.time()
    print(f"Operation took {end - start} seconds")
    return {"npcs_temp": npc_dict_temp}

@app.get("/npc_names")
async def get_npc_names(number: int = Query(default=5000, ge=1, le=50000)):
    #tempoarary measure to have only a certain number of items
    #in a semi-persistent list, this is for testing purposes
    trim_dict_items(persistant_npc_dict)

    # original function will come back to this later
    npc_na = npc_names(persistant_npc_dict)
    return {"npc_names": npc_na}