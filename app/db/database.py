from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:9428@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # ,connect_args={"check_same_thread": False} #only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


metadata = MetaData(schema='postgres')
Base = declarative_base(metadata=metadata)
