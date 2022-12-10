from operator import mod
from sqlalchemy.orm import Session

from . import models, schemas


def get_student_by_number(db: Session, student_number: str):

    return db.query(models.Student).filter(models.Student.registered_number == student_number).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Student(name=student.name, registred_number=student.registered_number)
    db_user = models.Student
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


    

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
