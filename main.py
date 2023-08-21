from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from crud import crud
from routers import login, operations, users

app = FastAPI(title="Pupuest", debut=True,
    description="Descripcion del proyecto",
    summary="Diego bobo",
    version="0.0.1",
    contact={
        "name": "Dario bobo",
        "url": "www.twitter.com/rektmin",
        "email": "diegomp96@gmail.com",
    },
)



app.include_router(login.router)
app.include_router(operations.router)
app.include_router(users.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    try:
        crud.get_db()
    finally:
        raise HTTPException(status_code=500, detail="Coudln't connect to the database.")
    raise HTTPException(status_code=200, detail="The backend is online.")    
