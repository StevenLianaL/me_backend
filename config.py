import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    # dir
    ROOT_DIR = PROJECT_ROOT_DIR = Path(os.path.realpath(__file__)).parent

    # sub app
    idiom_app_name = 'idiom'


project = Settings()
