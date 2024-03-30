from pydantic import BaseModel
from important_classes.npc import *
from typing import Dict, List, Union

class Npc_item(BaseModel):
    id: int
    name: str
    npc_race: str
    npc_subrace: str
    npc_class: str
    special_race_info: str
    stat_block: Dict[str, int]
    starting_pack: List[Union[str, List[str]]]