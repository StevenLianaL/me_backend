import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    # dir
    ROOT_DIR = PROJECT_ROOT_DIR = Path(os.path.realpath(__file__)).parent
    DATA_DIR = ROOT_DIR / 'data'
    # name space
    idiom_space = 'idiom'


project = Settings()
