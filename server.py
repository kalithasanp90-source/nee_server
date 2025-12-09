from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    user_sent_selfie: bool = False
    user_sent_voice: bool = False

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Nee Brain V2 server running"
    }

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        # Temporary response until model is connected
        reply_text = f"Née heard you say: {req.message}"
        return {"reply": reply_text}
    except Exception as e:
        return {"error": str(e)}    session = ort.InferenceSession(ONNX_PATH, providers=["CPUExecutionProvider"])

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
