from fastapi import APIRouter
from Endpoint_dicts.classes import *
from Endpoint_dicts.races import *



router = APIRouter()

@router.get("/api/classes")
async def classes():
    return{"classes": CLASS_DICT}

@router.get("/api/races")
async def races():
    return{"races": RACE_DICT}

