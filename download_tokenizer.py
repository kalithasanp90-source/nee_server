import os
import io
import zipfile
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def download_from_drive(file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"Downloading {file_id} ...")
    r = requests.get(url)
    r.raise_for_status()
    return r.content

# 1) Download HF model + tokenizer (Nee_V2.zip)
NEE_V2_DIR = os.path.join(BASE_DIR, "Nee_V2")
os.makedirs(NEE_V2_DIR, exist_ok=True)

zip_bytes = download_from_drive("127Ic7Zf1HC6NZ5CbVTfUo5EWgcbRzy09")  # Nee_V2.zip
with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
    z.extractall(NEE_V2_DIR)

print("✅ Extracted Nee_V2 HF model & tokenizer")

# 2) Download ONNX model file
NEE_V2_ONNX_DIR = os.path.join(BASE_DIR, "Nee_V2_ONNX")
os.makedirs(NEE_V2_ONNX_DIR, exist_ok=True)

onnx_bytes = download_from_drive("1HYwzmKIMoK0Zjyjk-Y847lEYLyl4wjea")  # model.onnx
onnx_path = os.path.join(NEE_V2_ONNX_DIR, "model.onnx")
with open(onnx_path, "wb") as f:
    f.write(onnx_bytes)

print(f"✅ Saved ONNX model to {onnx_path}")
