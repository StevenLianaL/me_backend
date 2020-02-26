from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.help.idiom_help import load_idioms, is_last_char_chinese
from app.interface.idiom_inreface import Idiom
from config import project

router = APIRouter()
name_space = project.idiom_space


@router.get('/s', response_model=List[Idiom])
async def get_idioms(word: str):
    last_char = word[-1]
    if not is_last_char_chinese(last_char):
        res = {'error': '请输入规范的汉字'}
        return JSONResponse(status_code=400, content=res)
    all_idioms = await load_idioms()
    match_idioms = [i for i in all_idioms if i['word'][0] == last_char]
    if len(match_idioms):
        return match_idioms
    else:
        res = {'error': f'查询首字为：{last_char} 的成语无结果'}
        return JSONResponse(status_code=400, content=res)
