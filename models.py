from pydantic import BaseModel
from important_classes.npc import *

class Npc_item(BaseModel):
    id: int
    name: str
    npc_race: str
    npc_subrace: str
    npc_class: str