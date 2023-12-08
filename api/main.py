from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World, workflow pipeline is working!'}

@app.get('/test/')
async def message():
    return {'message': 'Hello Lais, API está funcionando!'}

handler = Mangum(app=app)