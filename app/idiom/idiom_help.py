import json
from pathlib import Path

from app.idiom.idiom_config import idiom_config


async def load_idioms():
    file = Path(idiom_config.DATA_DIR, 'idiom.json')
    with file.open(encoding='utf8') as f:
        data = json.load(f)
    return data


def is_last_char_chinese(char: str):
    return True if '/u4e00' <= char <= '\u9fff' else False
