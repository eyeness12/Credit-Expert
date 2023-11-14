
from uvicorn import run
from fastapi import FastAPI
from source.apis.endpoints import credit_router
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4200", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    app.include_router(credit_router)
    run(app, host="localhost", port=5000)

