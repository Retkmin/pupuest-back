from fastapi import FastAPI

app = FastAPI(title="Pupuest", debut=True)

from routers import login

app.include_router(login.router)
