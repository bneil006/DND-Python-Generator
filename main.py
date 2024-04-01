from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from important_classes.npc import *
from logic.functional_logic import *
from models import *
import time



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

### PAGES ###
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/npc_gen")
async def npc_gen():
    return FileResponse("static/npc_gen.html")

## INTERNAL TEST ##
@app.get("/design")
async def design():
    return FileResponse("static/work.html")

from work import *
@app.get("/design_result")
async def design_result(brand: str = Query(default="Hanwha"), watt: int = Query(default=405), panel_count: float = Query(default=10), roof_size: float = Query(default=2000)):
    try:
        result = module_roof_percentage(brand, watt, panel_count, roof_size)
        return JSONResponse(content={"result": result})
    except KeyError:
        return JSONResponse(content={"error": "The specified panel size does not exist. Please enter a new size."}, status_code=400)

## INTERNAL TEST ##

### APIs ###
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

@app.get("/npc_generator")
async def get_npcs(number: int = Query(default=5, le=500)):
    start = time.time()
    create_npcs(number)
    end = time.time()
    print(f"Operation took {end - start} seconds")
    # Return your persistent NPC dictionary here
    return {"npcs": persistant_npc_dict}

@app.get("/npcs_generator_temp")
async def get_npcs_temp(number: int = Query(default=5, le=5000)):
    start = time.time()

    npc_dict_temp = create_npcs_temporary(number)
    
    end = time.time()
    print(f"Operation took {end - start} seconds")
    return {"npcs_temp": npc_dict_temp}

@app.get("/npc_names")
async def get_npc_names(number: int = Query(default=50000)):
    npc_list = npc_names(persistant_npc_dict)
    return {"npc_names": npc_list}

@app.get("/clear_npcs")
async def clear_npcs():
    # Clears the 'npc' dictionary
    persistant_npc_dict["npc"].clear()
    return {"message": "NPC dictionary cleared successfully."}