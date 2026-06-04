from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db, UserDB


app = FastAPI(title="Simple User API (SQLite-DB)")

#---Model---
class User(BaseModel):
    id: int
    username: str
    age: int
    class Config:
        from_attributes = True

#---POST: add User ----
@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    existing = db.query(UserDB).filter(UserDB.id == user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"User with id {user.id} already exists")

    db_user = UserDB(id=user.id, username=user.username, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully!", "user": db_user }

#---GET: all users or filter by id---
@app.get("/users")
def get_users(id:Optional[int] = Query(None, description="Filter by User ID"), db: Session = Depends(get_db)):
    if id is not None:
        user = db.query(UserDB).filter(UserDB.id == id).first()
        if not user:
            raise HTTPException(status_code=400, detail=f"User with id {id} does not exist")
        return user
    return db.query(UserDB).all()






