from fastapi import FastAPI, Query, HTTPException
from end_points import router as end_points_router
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from models import *
from npc import *



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(end_points_router)

### PAGES ###
@app.get("/")
async def root():
    return FileResponse("static/index.html")

#### APIs ####
@app.get("/gen_npc")
async def get_npcsss_temp(number: int = Query(default=5)):
    npc_dict_temp = create_random_npc_temp_dict(number)
    return {"npcs_temp": npc_dict_temp}


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