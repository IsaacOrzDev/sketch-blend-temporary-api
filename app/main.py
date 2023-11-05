from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import json

app = FastAPI()

load_dotenv()

origins = [
    "http://localhost:3000",
    "https://sketch-blend.isaacdev.net",
    "https://sketch-blend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def read_posts_data():
    with open('./data/posts.json', 'r') as file:
        data = json.load(file)
    return data


@app.get('/posts')
def getPosts():
    data = read_posts_data()
    return data


@app.get('/posts/{id}')
def getPost(id: str):
    data = read_posts_data()
    for post in data["records"]:
        if post['id'] == id:
            return {"record": post}
    return {"message": "Post not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
