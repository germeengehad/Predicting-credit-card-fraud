from fastapi import FastAPI
import uvicorn
from route.model import model_router
from config.settings import settings

app = FastAPI(
    title= 'FastAPI gmm model',
    descriptions='this is desc of our model'

)

app.include_router(model_router, tags=['gmm model'],prefix=settings.API_V1_STR)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=settings.DEBUG_MODE, host=settings.DOMAIN, port=settings.BACKEND_PORT)




















   