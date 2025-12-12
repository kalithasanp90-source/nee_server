from fastapi import FastAPI
from pydantic import BaseModel
from nee_core import NeeBrain

app = FastAPI()
brain = NeeBrain()


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    send_selfie: bool
    selfie_reason: str
    send_voice: bool
    voice_reason: str
    bond: float


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = brain.handle_message(req.message)
    return ChatResponse(**result)


@app.get("/")
def home():
    return {"status": "Née HF API Server Live"}
