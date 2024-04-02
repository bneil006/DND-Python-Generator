from fastapi import APIRouter
from endpoint_dicts.classes import *
from endpoint_dicts.races import *



router = APIRouter()

@router.get("/api/classes")
async def classes():
    return{"classes": CLASS_DICT}

@router.get("/api/races")
async def races():
    return{"races": RACE_DICT}

