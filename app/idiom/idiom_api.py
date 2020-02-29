from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.idiom.idiom_help import is_last_char_chinese, load_idioms
from app.idiom.idiom_interface import Idiom
from config import project

idiom_app = FastAPI(openapi_prefix=f"/{project.idiom_app_name}")

idiom_app.add_middleware(CORSMiddleware,
                         allow_origins=['*'], allow_credentials=True,
                         allow_methods=['*'], allow_headers=['*']
                         )


@idiom_app.get('/', response_model=List[Idiom])
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
