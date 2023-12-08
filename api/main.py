from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World, workflow pipeline is working!'}

handler = Mangum(app=app)