import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID, BIGINT, TEXT

from sqlalchemy.orm import relationship

from .database import Base

class Student(Base):

    __tablename__ = "student"

    id = Column(UUID, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(TEXT, nullable=False)
    registered_number = Column(TEXT, nullable=False)
                       
#                        Table "public.student"
#      Column     |  Type  | Collation | Nullable |      Default
# ----------------+--------+-----------+----------+-------------------
#  id             | uuid   |           | not null | gen_random_uuid()
#  name           | text   |           | not null |
#  student_number | bigint |           | not null |
# Indexes:
#     "student_pkey" PRIMARY KEY, btree (id)

class Professor(Base):

    __tablename__ = "professor"

    id = Column(UUID, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(TEXT, nullable=False) 

#                  Table "public.professor"
#  Column | Type | Collation | Nullable |      Default
# --------+------+-----------+----------+-------------------
#  id     | uuid |           | not null | gen_random_uuid()
#  name   | text |           | not null |


class Subject(Base):
    __tablename__ = "subject"

    id = Column(UUID, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(TEXT, nullable=False)
    professor_id = Column(UUID, nullable=False)

    # professor = relationship("Professor", back_)

#                    Table "public.subject"
#    Column   | Type | Collation | Nullable |      Default
# ------------+------+-----------+----------+-------------------
#  id         | uuid |           | not null | gen_random_uuid()
#  name       | text |           | not null |
#  student_id | uuid |           | not null |
# Indexes:
#     "subject_pkey" PRIMARY KEY, btree (id) 
