from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import MetaData, Session, SQLModel, create_engine

import data.core_aws_postgres.aws_db_models  # noqa: F401

dbuser = "postgres"
password = "axzCWh766"
host = "tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com"
port = "5432"
database = "postgres"

DATABASE_URI = f"postgresql://{dbuser}:{password}@{host}:{port}/{database}"

metadata = MetaData(schema="public")

connect_args = {"check_same_thread": False}
engine = create_engine(
    DATABASE_URI,
    echo=True,
    connect_args=connect_args
)

def get_session():
    with Session(engine) as session:
        yield session


Base = declarative_base()

SQLModel.metadata = Base.metadata
