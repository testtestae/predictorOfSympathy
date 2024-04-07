from src.core import core

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union

app = FastAPI()

from typing import List, Dict


class Person(BaseModel):
    id: int
    sympathyList: List[int]


class AllRequest(BaseModel):
    users: List[Person]


@app.post("/")
async def create_person(person: AllRequest):
    return core(person)
