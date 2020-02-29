from pydantic import BaseSettings

from config import project


class Settings(BaseSettings):
    # dir
    APP_NAME = project.idiom_app_name
    APP_DIR = project.ROOT_DIR / 'app' / f"{project.idiom_app_name}"
    DATA_DIR = APP_DIR / 'data'


idiom_config = Settings()
