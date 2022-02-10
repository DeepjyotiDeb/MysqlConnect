from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID


class Blogger(BaseModel): 
    title: str
    summary: str