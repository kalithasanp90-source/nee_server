from fastapi import FastAPI
from pydantic import BaseModel
from nee_core import NeeBrain

app = FastAPI()
brain = NeeBrain()

class Query(BaseModel):
    text: str

@app.post("/chat")
def chat(req: Query):
    reply = brain.generate(req.text)
    return {"reply": reply}

@app.get("/")
def root():
    return {"status": "Née Server Running!"}
