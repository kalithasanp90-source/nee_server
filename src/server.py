from fastapi import FastAPI
from pydantic import BaseModel
from nee_core import NeeBrain
import uvicorn

app = FastAPI()

brain = NeeBrain()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

        result = brain.handle_message(req.message)

        return ChatResponse(
            reply=result["reply_text"]
        )


@app.get("/")
def home():
    return {"status": "Née test server running"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
