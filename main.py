<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"He":"Uds"}

@app.get("/3s")
async def des():
    file_p="./exp4/e3s.c"
    return FileResponse(file_p)
    
@app.get("/3c")
async def des():
    file_p="./exp4/e3c.c"
    return FileResponse(file_p)

@app.get("/4s")
async def des():
    file_p="./exp4/e4s.c"
    return FileResponse(file_p)
    
@app.get("/4c")
async def des():
    file_p="./exp4/e4c.c"
    return FileResponse(file_p)

@app.get("/5s")
async def des():
    file_p="./exp4/e5s.c"
    return FileResponse(file_p)
    
@app.get("/5c")
async def des():
    file_p="./exp4/e5c.c"
    return FileResponse(file_p)
    
@app.get("/6s")
async def des():
    file_p="./exp4/e6s.c"
    return FileResponse(file_p)
    
@app.get("/6c")
async def des():
    file_p="./exp4/e6c.c"
    return FileResponse(file_p)
    
@app.get("/7s")
async def des():
    file_p="./exp4/e7s.c"
    return FileResponse(file_p)
    
@app.get("/7c")
async def des():
    file_p="./exp4/e7c.c"
    return FileResponse(file_p)
    
@app.get("/8s")
async def des():
    file_p="./exp4/e8s.c"
    return FileResponse(file_p)
    
@app.get("/8c")
async def des():
    file_p="./exp4/e8c.c"
    return FileResponse(file_p)
    
@app.get("/9s")
async def des():
    file_p="./exp4/e9s.c"
    return FileResponse(file_p)
    
@app.get("/9c")
async def des():
    file_p="./exp4/e9c.c"
    return FileResponse(file_p)
    
@app.get("/10")
async def des():
    file_p="./exp4/e10.c"
    return FileResponse(file_p)
=======
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"He":"Uds"}

@app.get("/3s")
async def des():
    file_p="./exp4/e3s.c"
    return FileResponse(file_p)
    
@app.get("/3c")
async def des():
    file_p="./exp4/e3c.c"
    return FileResponse(file_p)

@app.get("/4s")
async def des():
    file_p="./exp4/e4s.c"
    return FileResponse(file_p)
    
@app.get("/4c")
async def des():
    file_p="./exp4/e4c.c"
    return FileResponse(file_p)

@app.get("/5s")
async def des():
    file_p="./exp4/e5s.c"
    return FileResponse(file_p)
    
@app.get("/5c")
async def des():
    file_p="./exp4/e5c.c"
    return FileResponse(file_p)
    
@app.get("/6s")
async def des():
    file_p="./exp4/e6s.c"
    return FileResponse(file_p)
    
@app.get("/6c")
async def des():
    file_p="./exp4/e6c.c"
    return FileResponse(file_p)
    
@app.get("/7s")
async def des():
    file_p="./exp4/e7s.c"
    return FileResponse(file_p)
    
@app.get("/7c")
async def des():
    file_p="./exp4/e7c.c"
    return FileResponse(file_p)
    
@app.get("/8s")
async def des():
    file_p="./exp4/e8s.c"
    return FileResponse(file_p)
    
@app.get("/8c")
async def des():
    file_p="./exp4/e8c.c"
    return FileResponse(file_p)
    
@app.get("/9s")
async def des():
    file_p="./exp4/e9s.c"
    return FileResponse(file_p)
    
@app.get("/9c")
async def des():
    file_p="./exp4/e9c.c"
    return FileResponse(file_p)
    
@app.get("/10")
async def des():
    file_p="./exp4/e10.c"
    return FileResponse(file_p)





>>>>>>> 039c02266497662c03dde1acf9a08a91c326fdd9
