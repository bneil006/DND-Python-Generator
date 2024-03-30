from fastapi import FastAPI
from pydantic import BaseModel
from npcs.npc import *
from typing import Dict

class Npc_item(BaseModel):
    id: int
    name: str
    npc_race: str
    npc_subrace: str
    npc_class: str
    special_race_info: str
    stat_block: Dict[str, int]
    starting_pack: Dict 