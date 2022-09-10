from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware 
from db import session 
from model import TargetsTable

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def read_targets():
    users = session.query(TargetsTable).all()
    return users


@app.post("/target")
async def add_target(domain: str):
    target = TargetsTable()
    target.domain = domain
    target.statut = 0
    session.add(target)
    session.commit()


@app.put("/target")
async def update_target_statut(targets: List[TargetsTable]):
    for new_target in targets:
        target = session.query(TargetsTable).\
            filter(TargetsTable.id == new_target.id).first()
        target.name = new_target.name
        target.age = new_target.age
        session.commit()


@app.get("/target/{target_id}")
def read_user(target_id: int):
    target = session.query(TargetsTable).\
        filter(TargetsTable.id == target_id).first()
    return target