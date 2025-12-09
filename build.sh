#!/bin/bash
set -e

pip install gdown -q
mkdir -p Nee_V2

echo "Downloading ONNX model..."
gdown --fuzzy "https://drive.google.com/file/d/12F5s4htEf4OGSa4CoCG3r1m5H9jSlPGG/view" -O Nee_V2/model.onnx

echo "Downloading tokenizer..."
gdown --fuzzy "https://drive.google.com/file/d/1HYwzmKIMoK0Zjyjk-Y847lEYLyl4wjea/view" -O Nee_V2/tokenizer.json

pip install -r requirements.txt
