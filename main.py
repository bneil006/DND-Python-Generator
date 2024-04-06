from fastapi import FastAPI, Query, HTTPException
from end_points import router as end_points_router
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from models import *
from npc import *
import random
import os



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(end_points_router)

### PAGES ###
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/dungeon_generator")
async def dungeon_generator():
    return FileResponse("static/dungeon_generator.html")

#### APIs ####
@app.get("/gen_npc")
async def get_npcs_temp(number: int = Query(default=5, le=5000)):
    npc_dict_temp = create_random_npc_temp_dict(number)
    return {"npcs_temp": npc_dict_temp}

@app.get("/generate_dungeon")
async def generate_dungeon():
    # Assuming you have multiple GLTF files and want to pick one randomly
    dungeon_dir = "static/models/dungeons"  # Adjust path as necessary
    dungeon_files = [f for f in os.listdir(dungeon_dir) if f.endswith('.glb')]
    if not dungeon_files:
        raise HTTPException(status_code=404, detail="No dungeon models found")
    selected_dungeon = random.choice(dungeon_files)
    return FileResponse(path=os.path.join(dungeon_dir, selected_dungeon), media_type='model/gltf-binary')


#### INTERNAL TEST ####
@app.get("/design")
async def design():
    return FileResponse("static/work.html")

from work.work import *
@app.get("/design_result")
async def design_result(brand:str = Query(default="Hanwha"), watt:int = Query(default=405), panel_count:float = Query(default=10), roof_size:float = Query(default=2000)):
    try:
        result = module_roof_percentage(brand, watt, panel_count, roof_size)
        return JSONResponse(content={"result": result})
    except KeyError:
        return JSONResponse(content={"error": "The specified panel size does not exist. Please enter a new size."}, status_code=400)
#### INTERNAL TEST ####