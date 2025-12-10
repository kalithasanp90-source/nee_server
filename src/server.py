from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from nee_core import NeeBrain

app = FastAPI()

# CORS (allow Unity, web, mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load AI
nee = NeeBrain()

@app.get("/")
def home():
    return {"status": "Née Server Running"}

@app.post("/chat")
async def chat_api(data: dict):
    msg = data.get("message", "")
    reply = nee.chat(msg)
    return {"reply": reply}
