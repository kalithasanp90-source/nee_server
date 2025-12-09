from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import os
import traceback

app = FastAPI()

# --- Simple debug exception handler so we see runtime error messages directly ---
@app.exception_handler(Exception)
async def debug_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"debug_error": str(exc), "trace": traceback.format_exc()})

@app.get("/")
async def root():
    return {"status": "ok", "message": "Nee Brain V2 server running"}

# Chat request model — match your nee_core.py usage
class ChatRequest(BaseModel):
    user_id: str
    message: str
    user_sent_selfie: bool = False
    user_sent_voice: bool = False

class ChatResponse(BaseModel):
    reply: str
    send_selfie: bool = False
    selfie_reason: str = "none"
    send_voice: bool = False
    voice_reason: str = "none"
    bond: float = 0.0

# Lazy-load model/tokenizer when first chat arrives (saves startup time)
MODEL = None
TOKENIZER = None
SESSION = None
LOADED = False

import os

print("Tokenizer file size:", os.path.getsize("Nee_V2/tokenizer.json"))

def load_resources():
    global MODEL, TOKENIZER, LOADED
    if LOADED:
        return
    # load tokenizer from Nee_V2 folder and ONNX from Nee_V2_ONNX/model.onnx
    from transformers import AutoTokenizer
    import onnxruntime as ort
    tok_dir = os.path.join(os.getcwd(), "Nee_V2")
    onnx_path = os.path.join(os.getcwd(), "Nee_V2_ONNX", "model.onnx")
    TOKENIZER = AutoTokenizer.from_pretrained(tok_dir, trust_remote_code=False)
    # Create ONNX session
    SESSION = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    LOADED = True
    globals().update({"TOKENIZER": TOKENIZER, "SESSION": SESSION})

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        load_resources()
        # Simple echo-style response using tokenizer for demo.
        # Replace this block with your nee_core inference pipeline using SESSION and TOKENIZER.
        user_msg = req.message
        # placeholder reply logic (replace with model inference)
        reply = f"Née (demo): I heard '{user_msg}' — I will be bold and teasing!"
        return ChatResponse(reply=reply, send_selfie=False, selfie_reason="none", send_voice=False, voice_reason="none", bond=4.0)
    except Exception as e:
        raise e
