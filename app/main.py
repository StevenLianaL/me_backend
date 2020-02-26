from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import idiom_api
from config import project

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=['*'], allow_credentials=True,
                   allow_methods=['*'], allow_headers=['*']
                   )

app.include_router(idiom_api.router, prefix=project.idiom_space, tags=[project.idiom_space])
