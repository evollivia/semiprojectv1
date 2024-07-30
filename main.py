from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.routes.member import member_router
from app.routes.board import board_router

app = FastAPI()
templates = Jinja2Templates(directory="views/templates")  # jinja2 설정
app.mount('/static', StaticFiles(directory='views/static'), name='static')

# 외부 라우트 생성
app.include_router(member_router, prefix='/member')
app.include_router(board_router, prefix='/board')


# index 라우트
@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})
