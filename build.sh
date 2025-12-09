#!/bin/bash
set -e

# Install downloader
pip install --no-cache-dir gdown -q

# Create folders
mkdir -p Nee_V2 Nee_V2_ONNX

echo "Downloading tokenizer ZIP from Google Drive..."
# Replace TOKENIZER_ID if yours is different
gdown --fuzzy "https://drive.google.com/uc?id=12F5s4htEf4OGSa4CoCG3r1m5H9jSlPGG" -O Nee_V2/tokenizer.zip

echo "Extracting tokenizer..."
unzip -o Nee_V2/tokenizer.zip -d Nee_V2

echo "Downloading ONNX model from Google Drive..."
# Replace MODEL_ID if yours is different
gdown --fuzzy "https://drive.google.com/uc?id=1HYwzmKIMoK0Zjyjk-Y847lEYLyl4wjea" -O Nee_V2_ONNX/model.onnx

echo "Verifying files..."
python - <<'PY'
import os,sys,json
tk = "Nee_V2/tokenizer.json"
if os.path.exists(tk):
    print("tokenizer.json size:", os.path.getsize(tk))
else:
    print("WARNING: tokenizer.json not found in Nee_V2/")
print("model.onnx size:", os.path.getsize("Nee_V2_ONNX/model.onnx") if os.path.exists("Nee_V2_ONNX/model.onnx") else "MISSING")
PY

echo "Installing python requirements..."
pip install --no-cache-dir -r requirements.txt

echo "Build script finished."
