import json
from pathlib import Path

from config import project


async def load_idioms():
    file = Path(project.DATA_DIR, project.idiom_space, 'idiom.json')
    with file.open(encoding='utf8') as f:
        data = json.load(f)
    return data


def is_last_char_chinese(char: str):
    return True if '/u4e00' <= char <= '\u9fff' else False

