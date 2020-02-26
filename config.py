import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    ROOT_DIR = PROJECT_ROOT_DIR = Path(os.path.realpath(__file__)).parent
