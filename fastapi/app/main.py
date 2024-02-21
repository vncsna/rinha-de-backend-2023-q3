from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy import func, or_, any_
from sqlalchemy.orm import Session

from app.db import Person, get_session


app = FastAPI()


class PersonCreate(BaseModel):
    apelido: str
    nome: str
    nascimento: str
    stack: List[str] = []


@app.get("/pessoas")
def get_person(t: str, session: Session = Depends(get_session)):
    return (
        session
        .query(Person)
        .filter(or_(
            Person.nome.ilike(f"%{t}%"),
            Person.apelido.ilike(f"%{t}%"),
            func.array_to_string(Person.stack, ",", "").ilike(f"%{t}%"),
        ))
        .limit(50)
        .all()
    )


@app.get("/pessoas/{person_id}")
def get_person_by_id(person_id: int, session: Session = Depends(get_session)):
    return session.query(Person).filter_by(id=person_id).one()


@app.get("/contagem-pessoas")
def get_person_count(session: Session = Depends(get_session)):
    return session.query(func.count(Person.id)).scalar()


@app.post("/pessoas")
def create_person(body: PersonCreate, session: Session = Depends(get_session)):
    person = Person(**body.model_dump())
    session.add(person)
    return JSONResponse(
        {},
        status_code=201,
        headers={"Location": f"/pessoas/{person.id}"},
    )
