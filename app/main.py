from fastapi import FastAPI

from app.idiom.idiom_api import idiom_app
from config import project

app = FastAPI()

app.mount(f"/{project.idiom_app_name}", idiom_app)
