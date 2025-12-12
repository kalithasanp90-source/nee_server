import os
import onnxruntime as ort
from huggingface_hub import hf_hub_download

MODEL_REPO = "Neelan12/Neelan"
MODEL_FILE = "model.onnx"

class NeeBrain:
    def __init__(self):
        # get HF token set in Render environment
        token = os.getenv("HF_TOKEN")
        if not token:
            raise ValueError("HF_TOKEN is not set in Render!")

        # download ONNX model from private repo
        print("Downloading model from HuggingFace...")
        model_path = hf_hub_download(
            repo_id=MODEL_REPO,
            filename=MODEL_FILE,
            token=token
        )

        print("Model downloaded:", model_path)

        # ONNX runtime session
        self.session = ort.InferenceSession(model_path)

    def generate(self, text: str):
        # Dummy output now — replace with your real model input/output later
        return f"Née heard: {text}"
