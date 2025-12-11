import os
import json
import onnxruntime as ort


# ------------------------------------------
# PATH SETUP
# ------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model.onnx")
TOKEN_DIR = os.path.join(BASE_DIR, "Nee_V2")

VOCAB_PATH = os.path.join(TOKEN_DIR, "vocab.json")
TOKENIZER_JSON = os.path.join(TOKEN_DIR, "tokenizer.json")
SPECIAL_TOKENS = os.path.join(TOKEN_DIR, "special_tokens_map.json")
TOKENIZER_CONFIG = os.path.join(TOKEN_DIR, "tokenizer_config.json")
MERGES_PATH = os.path.join(TOKEN_DIR, "merges.txt")


# ------------------------------------------
# LOAD TOKENIZER FILES
# ------------------------------------------

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class SimpleTokenizer:
    def __init__(self):

        self.vocab = load_json(VOCAB_PATH)
        self.tokenizer_json = load_json(TOKENIZER_JSON)

        # Basic reverse vocab for decoding
        self.id_to_token = {v: k for k, v in self.vocab.items()}

    def encode(self, text):
        # Super-simple tokenization (placeholder)
        tokens = text.strip().split()
        ids = [self.vocab.get(t, self.vocab.get("<unk>", 0)) for t in tokens]
        return ids

    def decode(self, ids):
        tokens = [self.id_to_token.get(i, "<unk>") for i in ids]
        return " ".join(tokens)


# ------------------------------------------
# LOAD ONNX MODEL
# ------------------------------------------

class NeeBrain:

    def __init__(self):
        print("🔄 Loading ONNX model...")

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")

        self.session = ort.InferenceSession(MODEL_PATH)

        print("✅ Model loaded!")

        # Load tokenizer
        self.tokenizer = SimpleTokenizer()
        print("✅ Tokenizer loaded!")

    # ------------------------------------------------
    # Simple test function for checking if server works
    # ------------------------------------------------
    def think(self, text):
        """
        Basic inference pipeline – replace later with real logic.
        """

        # Encode input
        ids = self.tokenizer.encode(text)

        # ONNX expects input name
        input_name = self.session.get_inputs()[0].name

        # Run inference
        output = self.session.run(None, {input_name: [ids]})

        # Return dummy + output length
        return {
            "input": text,
            "encoded": ids,
            "output_length": len(output[0][0]),
            "message": "Inference success (dummy output)."
        }
