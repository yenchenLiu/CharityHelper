from typing import List, Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class CharityBase(BaseModel):
    name: str


class Charity(CharityBase):
    id: int
    tags: List[Tag] = []

    class Config:
        orm_mode = True
