from fastapi import APIRouter

from domain.features.user_auth.login.login_router import router as login_router
from domain.features.user_auth.logout.logout_router import \
    router as logout_router
from domain.features.user_auth.register.register_router import \
    router as register_router

router = APIRouter(prefix="/user_auth", tags=["User auth"])

router.include_router(login_router)
router.include_router(register_router)
router.include_router(logout_router)