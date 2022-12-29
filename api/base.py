from fastapi import APIRouter

from api import route_users, route_dweets, route_login


api_router = APIRouter()
api_router.include_router(route_users.router, prefix='/accounts', tags=['accounts'])
api_router.include_router(route_login.router, prefix='/login', tags=['login'])
api_router.include_router(route_dweets.router, prefix='/dweets', tags=['dweets'])