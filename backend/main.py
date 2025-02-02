from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    response = f"AI Response to: {query.question}"
    return {"answer": response}

@app.get("/")
def home():
    return {"message": "Welcome to ITA AI!"}
