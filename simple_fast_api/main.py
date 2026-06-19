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

#--- Schema for updates--
class UserUpdate(BaseModel):
    username: Optional[str] = None
    age: Optional[int] = None

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

#--PUT : update existing user
@app.put("/users/{user_id}")
def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail=f"User with id {user_id} does not exist")

        if updates.username is not None:
            user.username = updates.username
        if updates.age is not None:
            user.age = updates.age

        db.commit()
        db.refresh(user)
        return{"message": "User updated successfully!", "user": user }
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f'Unexpected error: {str(e)}')








