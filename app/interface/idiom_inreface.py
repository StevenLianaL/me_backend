from pydantic import BaseModel


class Idiom(BaseModel):
    word: str
    derivation: str  # 出处
    example: str
    explanation: str
    pinyin: str
    abbreviation: str  # 拼音首字母
