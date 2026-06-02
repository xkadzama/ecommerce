from fastapi import FastAPI

from app.routing import categories
from app.routing import products

app = FastAPI(title='FastAPI интернет магазин', version='0.1.0')

app.include_router(categories.router)
app.include_router(products.router)

@app.get('/')
async def root():
	return {'message': 'Главная страница!'}