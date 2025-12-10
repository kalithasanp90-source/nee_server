from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from nee_core import NeeBrain

app = FastAPI()

# Load brain once
brain = NeeBrain()


# ---------- Request Body ----------
class ChatRequest(BaseModel):
    user_id: str
    message: str
    user_sent_selfie: bool = False
    user_sent_voice: bool = False


# ---------- Response Format ----------
class ChatResponse(BaseModel):
    reply: str
    send_selfie: bool
    selfie_reason: str
    send_voice: bool
    voice_reason: str
    bond: float


# ---------- Route ----------
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    result = brain.handle_message(
        user_text=req.message,
        user_sent_selfie=req.user_sent_selfie,
        user_sent_voice=req.user_sent_voice
    )

    return ChatResponse(
        reply=result["reply_text"],
        send_selfie=result["send_selfie"],
        selfie_reason=result["selfie_reason"],
        send_voice=result["send_voice"],
        voice_reason=result["voice_reason"],
        bond=result["bond"],
    )


@app.get("/")
def home():
    return {"status": "Née V2 Server Live"}


# ---------- MAIN ----------
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
