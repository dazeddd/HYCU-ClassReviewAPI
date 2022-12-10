from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    registered_number: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: str

    class Config:
        orm_mode=True


class ProfessorBase(BaseModel):
    name: str


class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: str

    class Config:
        orm_mode=True


class SubjectBase(BaseModel):
    name: str    

class Subject(SubjectBase):
    id: str
    name: str
    professor_id: Professor

    class Config:
        orm_mode = True
