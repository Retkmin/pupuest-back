
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from api.data.core_aws_postgres.aws_database_config import get_session
from api.data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from api.data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    get_users_list_test,
)
from api.domain.features.user_auth.user_auth_router import (
    router as user_auth_router,
)

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

app.include_router(user_auth_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    raise HTTPException(status_code=200, detail="The backend is online.")

@app.get("/test_users_list", response_model=list[UserInfo])
async def test_users_list(session: Session = Depends(get_session)):
    return get_users_list_test(session=session)