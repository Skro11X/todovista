from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas import Task, TaskCreate
# from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
# from app import crud

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("/active", response_model=List[Task])
def get_active_tasks():
    """Get all active (not completed) tasks"""
    # db: Session = Depends(SessionLocal)
    # return crud.get_active_tasks(db)
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/closed", response_model=List[Task])
def get_closed_tasks():
    """Get all closed (completed) tasks"""
    # db: Session = Depends(SessionLocal)
    # return crud.get_closed_tasks(db)
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    """Create a new task"""
    # db: Session = Depends(SessionLocal)
    # return crud.create_task(db, task)
    raise HTTPException(status_code=501, detail="Not implemented") 