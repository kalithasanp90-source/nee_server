import os
from transformers import AutoTokenizer
import onnxruntime as ort


class NeeBrain:
    def __init__(self):
        # Build absolute paths
        BASE = os.path.dirname(os.path.abspath(__file__))

        self.TOKENIZER_DIR = os.path.join(BASE, "Nee_V2")
        self.MODEL_PATH = os.path.join(BASE, "model.onnx")

        print("== LOADING TOKENIZER FROM ==")
        print(self.TOKENIZER_DIR)

        print("== LOADING MODEL FROM ==")
        print(self.MODEL_PATH)

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.TOKENIZER_DIR)

        # Load ONNX model
        self.session = ort.InferenceSession(self.MODEL_PATH)

    def handle_message(self, user_text, **kwargs):

        # Just test if model + tokenizer work
        enc = self.tokenizer(user_text, return_tensors="np")

        # Run ONNX forward pass
        out = self.session.run(None, {
            "input_ids": enc["input_ids"],
            "attention_mask": enc["attention_mask"]
        })

        # Simple dummy reply
        reply = f"Née heard: {user_text}"

        return {
            "reply_text": reply,
            "send_selfie": False,
            "selfie_reason": "",
            "send_voice": False,
            "voice_reason": "",
            "bond": 0.5
        }
