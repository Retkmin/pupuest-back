from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import MetaData, SQLModel, create_engine

from models import (currency, invoice, language, operation,  # noqa: F401
                    payment_method, theme, token, user, user_info)

dbuser = "postgres"
password = "axzCWh766"
host = "tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com"
port = "5432"
database = "postgres"

#DATABASE_URI: str = ("postgresql://" + user + ":" + password + "@" + host + "/" + database)

#DATABASE_URI = "postgresql://postgres:axzCWh766@tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com/postgres"

DATABASE_URI = f"postgresql://{dbuser}:{password}@{host}:{port}/{database}"
metadata = MetaData(schema="public")

engine = create_engine(
    DATABASE_URI,
    connect_args={"options": "-csearch_path=public"}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
SQLModel.metadata = Base.metadata

#SQLModel.metadata.create_all(engine)