import os, traceback
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

TOKENIZER_DIR = os.path.join(os.getcwd(), "Nee_V2")
ONNX_PATH = os.path.join(os.getcwd(), "Nee_V2_ONNX", "model.onnx")

@app.exception_handler(Exception)
async def debug_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"error": str(exc), "trace": traceback.format_exc()})

@app.get("/")
def root():
    info = {
        "tokenizer_exists": os.path.exists(os.path.join(TOKENIZER_DIR, "tokenizer.json")),
        "tokenizer_files": os.listdir(TOKENIZER_DIR) if os.path.exists(TOKENIZER_DIR) else [],
        "onnx_exists": os.path.exists(ONNX_PATH),
        "onnx_size": os.path.getsize(ONNX_PATH) if os.path.exists(ONNX_PATH) else None
    }
    return info

class ChatReq(BaseModel):
    user_id: str
    message: str
    user_sent_selfie: bool = False
    user_sent_voice: bool = False

@app.post("/chat")
async def chat(r: ChatReq):
    # Lazy-load tokenizer & ONNX when first used to save startup time
    try:
        from transformers import AutoTokenizer
        import onnxruntime as ort
    except Exception as e:
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
