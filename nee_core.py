import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL_ID = "Neelan12/Neelan"   # your private HF model

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not set in Render!")

API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}


class NeeBrain:
    def __init__(self):
        print("🔥 Using HuggingFace Inference API (no ONNX needed).")

    def generate(self, prompt: str):
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code != 200:
            return f"⚠️ HF API Error: {response.text}"

        try:
            return response.json()[0]["generated_text"]
        except:
            return str(response.json())

    def handle_message(self, user_text, user_sent_selfie=False, user_sent_voice=False):
        reply = self.generate(user_text)

        return {
            "reply_text": reply,
            "send_selfie": False,
            "selfie_reason": "",
            "send_voice": False,
            "voice_reason": "",
            "bond": 0.5,
    }
