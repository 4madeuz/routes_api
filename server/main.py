from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from fastapi import FastAPI
from src.api import routes

app = FastAPI(
    title='Routes',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://client:5173",
    "http://client:8080",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/routes", tags=["routes"])


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000,
    )
