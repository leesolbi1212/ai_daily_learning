from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse #응답 주는 애
from fastapi.staticfiles import StaticFiles # url에서 static을 확인할 수 있게
from fastapi.templating import Jinja2Templates #

app = FastAPI()

# 정적 파일 (JS, CSS 등) 제공
# http://localhost:8080/static으로 접근했을 때 static 폴더에 접근할 수 있다.
# 외부에서 static이라는 이름으로 접근하겠다 (코드에서 접근할 때)
app.mount("/static",StaticFiles(directory="static"), name="static")

# html 템플릿 디렉토리
templates = Jinja2Templates(directory="templates")

# =========== Fast API 문법 ==================
# html 페이지 제공
@app.get("/", response_class=HTMLResponse) # 이렇게 호출을 받으면 사용자에게 전달할 때엔 HTMLResponse로 전달해줄거야. 진자 쓰겠다는 뜻 
async def get_page(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

# 백엔드 API – JSON 데이터 제공


@app.get("/api/data")
async def get_data():
    return{"message":"FastAPI에서 보내는 데이터입니다."}