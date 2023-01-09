from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.base import api_router
from db.session import engine
from db.base_class import Base


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount('/static', StaticFiles(directory='static'), name='static')


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(CORSMiddleware, allow_origins=["*"],
                       allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])
    include_router(app)
    configure_static(app)
    # create_tables()
    return app


app = start_application()
