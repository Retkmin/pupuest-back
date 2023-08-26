from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import MetaData, SQLModel, create_engine

import data.db_models  # noqa: F401

dbuser = "postgres"
password = "axzCWh766"
host = "tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com"
port = "5432"
database = "postgres"

DATABASE_URI = f"postgresql://{dbuser}:{password}@{host}:{port}/{database}"

metadata = MetaData(schema="public")

engine = create_engine(
    DATABASE_URI,
    connect_args={"options": "-csearch_path=public"}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
SQLModel.metadata = Base.metadata