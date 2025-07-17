from fastapi import FastAPI
from pydantic import BaseModel # 쉽게 json 형태로 만들어줌 원래 클래스는 속성과 메서드로 이루어져 있는데 속성을 넣으면 그걸 쉽게 json으로 바꿔주는 역할 

users = {
    0: {"userid": "apple", "name": "김사과"},
    1: {"userid": "banana", "name": "반하나"},
    2: {"userid": "orange", "name": "오렌지"}
}

application = FastAPI()

# 유저 조회하기
# http://127.0.0.1:8000/users/0
# uvicorn server:application --reload

@application.get("/users/{id}")
def find_user(id:int):
    user = users.get(id)
    if user is None:
        return {"error": "해당 id 없음"}
    return user

# 사용자 필드 조회 
# http://127.0.0.1:8000/users/1/userid -> "banana"
# http://127.0.0.1:8000/users/2/name -> "오렌지"

@application.get("/users/{id}/{key}") #경로의 값을 보내는 것 (자원의 위치를 명확히 표현할 때)

#REST API의 핵심은 자원의 위치(URL)를 명확히 정의하는 것인데,
#필수적이고 핵심적인 값은 경로로, 선택적이고 옵션적인 값은 쿼리로 표현하는 게 표준적인 방식
def find_user_by_key(id:int, key:str):
    user = users.get(id)
    if user is None or key not in user:
        return {"error": "잘못된 id 또는 key"}
    return user[key]

# 이름으로 사용자 조회
# http://127.0.0.1:8000/id-by-name?name=반하나


@application.get("/id-by-name") # value 값을 보내는 것 (추가적이고 선택적인 조건을 붙일 때)
def find_user_by_name(name:str): # 이름을 집어넣으면
    for idx, user in users.items(): # items = 키와 값을 같이 뽑아올 수 있음
        if user['name'] == name:
            return user
    return {"error" : "데이터를 찾지 못함"}

# 사용자 생성
class User(BaseModel):
    userid: str
    name: str
    
@application.post("/users/{id}")
def create_user(id:int, user:User):
    if id in users:
        return {"error": "이미 존재하는 키"}
    users[id] = user.model_dump() #복사해서 만드는 역할
    return {"success": "ok"}

# 사용자 수정
class UserForUpdate(BaseModel):
    userid: str | None = None # 값이 들어올 수도 있고, 안들어올 수도 있음!
    name: str | None = None
    
@application.put("/users/{id}")
def update_user(id: int, user: UserForUpdate):
    if id not in users:
        return {"error": "id가 존재하지 않음"}
    
    if user.userid is not None:
        users[id]["userid"] = user.userid
    if user.name is not None:
        users[id]["name"] = user.name
    
    return {"success": "ok"}

# 사용자 삭제 
@application.delete("/users/{id}")
def delete_user(id:int):
    if id not in users:
        return {"error": "존재하지 않는 사용자"}
    users.pop(id)
    return {"success": "ok"}