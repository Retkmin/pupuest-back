from sqlmodel import MetaData, Session, create_engine

#"postgresql://user:password@postgresserver/db"
user="postgres"
password="axzCWh766"
url="tradesage-dev.c0xcfmrj3pzo.us-east-2.rds.amazonaws.com/"
port="5432"
database="tradesage-dev"

DATABSE_URI: str = "postgresql+psycopg2://"+user+":"+password+"@"+url+":"+port+"/"+database

#conn = psycopg2.connect(DATABSE_URI)

metadata = MetaData(schema="public")


engine = create_engine(DATABSE_URI)

def get_session():
    with Session(engine) as session:
        yield session
    