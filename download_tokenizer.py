import os
import io
import zipfile
import requests
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEE_V2_DIR = os.path.join(BASE_DIR, "Nee_V2")
NEE_ONNX_DIR = os.path.join(BASE_DIR, "Nee_V2_ONNX")
os.makedirs(NEE_V2_DIR, exist_ok=True)
os.makedirs(NEE_ONNX_DIR, exist_ok=True)

def download_file_from_drive(file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"Downloading: {file_id}")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    return r.content

# --- Replace these with your file IDs (already set) ---
TOKENIZER_ZIP_ID = "12F5s4htEf4OGSa4CoCG3r1m5H9jSlPGG"
ONNX_ID = "1HYwzmKIMoK0Zjyjk-Y847lEYLyl4wjea"

# 1) Download & extract tokenizer ZIP
try:
    data = download_file_from_drive(TOKENIZER_ZIP_ID)
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            print("ZIP detected — extracting to Nee_V2/")
            z.extractall(NEE_V2_DIR)
            print("✓ Extracted ZIP contents into", NEE_V2_DIR)
    except zipfile.BadZipFile:
        # If it's a single file (e.g., tokenizer.json), save it.
        single_path = os.path.join(NEE_V2_DIR, "tokenizer.json")
        with open(single_path, "wb") as f:
            f.write(data)
        print("✓ Saved single tokenizer file to", single_path)
except Exception as e:
    print("ERROR while downloading/extracting tokenizer ZIP:", str(e))
    sys.exit(1)

# 2) Download ONNX
try:
    onnx_bytes = download_file_from_drive(ONNX_ID)
    onnx_path = os.path.join(NEE_ONNX_DIR, "model.onnx")
    with open(onnx_path, "wb") as f:
        f.write(onnx_bytes)
    print("✓ Saved ONNX model to", onnx_path)
except Exception as e:
    print("ERROR while downloading ONNX:", str(e))
    sys.exit(1)

print("All downloads complete.")
