from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import json
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080",
                   "http://127.0.0.1:8081",
                   "http://localhost:8080",
                   "http://localhost:8081",
                   "https://qxuzd.csb.app"],


    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Receptenator"


@app.get("/recepten")
def get_recepten():
    with open('../data/recepten.json') as file:
        data = json.load(file)

    return data


@app.get("/randomrecept")
def get_recepten():
    with open('../data/recepten.json') as file:
        data = json.load(file)

    return data[random.randint(0, len(data) - 1)]
