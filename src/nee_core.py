import os
import onnxruntime as ort
from transformers import AutoTokenizer

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(__file__)    # /opt/render/project/src/
MODEL_PATH = os.path.join(BASE_DIR, "model.onnx")
TOKENIZER_PATH = os.path.join(BASE_DIR, "Nee_V2")

print("MODEL PATH:", MODEL_PATH)
print("TOKENIZER PATH:", TOKENIZER_PATH)

# -----------------------------
# LOAD MODEL + TOKENIZER
# -----------------------------
class NeeBrain:
    def __init__(self):
        # Load tokenizer from Nee_V2 folder
        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

        # ONNX Runtime options
        session_options = ort.SessionOptions()
        session_options.intra_op_num_threads = 1

        print("Loading ONNX model...")
        self.session = ort.InferenceSession(
            MODEL_PATH,
            sess_options=session_options,
            providers=["CPUExecutionProvider"]
        )

    # -----------------------------
    # MAIN CHAT FUNCTION
    # -----------------------------
    def chat(self, message: str) -> str:
        # Tokenize input
        inputs = self.tokenizer(
            message,
            return_tensors="np",
            padding=True,
            truncation=True
        )

        # Run inference
        ort_inputs = {self.session.get_inputs()[0].name: inputs["input_ids"]}
        outputs = self.session.run(None, ort_inputs)

        # Decode (dummy for now)
        # Replace with your model's output mapping later
        reply_ids = outputs[0][0]
        reply_text = self.tokenizer.decode(reply_ids, skip_special_tokens=True)

        return reply_text
