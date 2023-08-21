from sqlmodel import MetaData, Session, create_engine

# "postgresql://user:password@postgresserver/db"
user = "postgres"
password = "axzCWh766"
postgresserver = "tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com/"
port = "5432"
database = "tradesage-dev"

DATABSE_URI: str = (
    "postgresql://"
    + user
    + ":"
    + password
    + "@"
    + postgresserver
    + ":"
    + port
    + "/"
    + database
)

metadata = MetaData(schema="public")

engine = create_engine(DATABSE_URI)


def get_session():
    with Session(engine) as session:
        yield session
