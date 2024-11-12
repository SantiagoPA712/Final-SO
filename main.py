from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from datetime import datetime

app = FastAPI()

class UserData(BaseModel):
    nombre: str
    edad: int
    profesion: str

@app.post("/store_data/")
async def store_data(user_data: UserData):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"/mnt/c/Users/santi/Desktop/Final SO/data/{timestamp}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        json.dump(user_data.dict(), file)

    return {"mensaje": "Datos guardados exitosamente", "archivo": filename}
