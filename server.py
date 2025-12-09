import os, traceback
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import onnxruntime as ort
from transformers import AutoTokenizer

app = FastAPI()

TOKENIZER_DIR = os.path.join(os.getcwd(), "Nee_V2")
MODEL_PATH = os.path.join(os.getcwd(), "Nee_V2_ONNX", "model.onnx")

@app.get("/")
def root():
    return {
        "tokenizer_files": os.listdir(TOKENIZER_DIR),
        "model_exists": os.path.exists(MODEL_PATH),
        "model_size": os.path.getsize(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
    }

class ChatReq(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(req: ChatReq):
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR, trust_remote_code=False)
    session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])

    # TEMP: echo only until full pipeline ready
    return {"reply": f"Née heard: {req.message}"}    except Exception as e:
        raise e

    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR, trust_remote_code=False)
    # load onnx session
    session = ort.InferenceSession(ONNX_PATH, providers=["CPUExecutionProvider"])

    # For safety: simple echo (replace with your real inference pipeline)
    return {"reply": f"Née (demo): I heard '{r.message}'", "user_id": r.user_id}LOADED = False

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
