from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    user_sent_selfie: bool
    user_sent_voice: bool

@app.get("/")
def root():
    return {"status": "ok", "message": "Nee Brain V2 server running"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        return {"reply": f"Née heard: {req.message}"}
    except Exception as e:
        return {"error": str(e)}
