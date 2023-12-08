from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World, workflow pipeline is working!'}

@app.get('/test/')
async def message1():
    return {'message': 'Hello Lais, API is working!'}

@app.get('/test/pt/')
async def message2():
    return {'message': 'Hello Lais, API está funcionando!'}

@app.get('/test/fr/')
async def message3():
    return {'message': 'Hello Lais, l\'API fonctionne!'}


handler = Mangum(app=app)