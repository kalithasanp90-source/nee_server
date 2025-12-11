from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .nee_core import NeeBrain  # nee_core.py is in the same src folder

app = FastAPI()

# Allow any origin (for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Single global brain
brain = NeeBrain()

@app.get("/")
async def root():
    return {"status": "ok", "message": "Nee server running"}

@app.post("/chat")
async def chat(body: dict):
    text = body.get("message", "")
    result = brain.handle_message(text)
    # Just return reply_text for now
    return {"reply": result["reply_text"]}
