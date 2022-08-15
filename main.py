from fastapi import FastAPI

app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/data")
def data():
    return {'hello' : 1234}

from pydantic import BaseModel
class msg(BaseModel):
    name : str
    phone : int

@app.post("/send")
def send(data: msg):
    print(data)
    return '전송완료'
