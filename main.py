from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from data.core_aws_postgres.aws_database_config import get_session
from data.core_aws_postgres.aws_db_models.user.user_crud import get_users_list_test
from domain.features.login.login_router import router as login_feature

app = FastAPI(
    title="Pupuest",
    debug=True,
    description="Descripcion del proyecto",
    summary="Diego bobo",
    version="0.0.1",
    contact={
        "name": "Rektmin",
        "email": "diegomp96@gmail.com"
    }
)

app.include_router(login_feature)

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
    raise HTTPException(status_code=200, detail="The backend is online.")

@app.get("/test_users_list")
async def test_users_list(session: Session = Depends(get_session)):
    return get_users_list_test(session=session)