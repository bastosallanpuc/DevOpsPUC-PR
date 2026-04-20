from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return {"message": "Deu boa"}

@app.get("/teste2")
async def funcaoteste2():
    return {"teste": True, "num_aleatorio": 1}