from sqlmodel import MetaData, Session, create_engine

dbuser = "backend"
password = "1234"
host = "tradinglab-main.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com"
port = "5432"
database = "postgres"

DATABASE_URI = f"postgresql://{dbuser}:{password}@{host}:{port}/{database}"

metadata = MetaData(schema="public")

#connect_args = {"check_same_thread": False}
engine = create_engine(
    DATABASE_URI,
    echo=True,
    #connect_args=connect_args
)

def get_session():
    with Session(engine) as session:
        yield session