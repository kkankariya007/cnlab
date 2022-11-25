from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

path="cn lab api"

@app.get("/")
async def root():
    return {"He":"Uds"}
    
@app.get("/1")
async def des():
    file_p="exp4\exp4_server.c"
    return FileResponse(file_p)




