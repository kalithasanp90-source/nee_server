#!/bin/bash
set -e

pip install --no-cache-dir gdown -q

# Create folder for ONNX
mkdir -p Nee_V2_ONNX

echo "Downloading ONNX model..."
gdown --fuzzy "https://drive.google.com/uc?id=1HYwzmKIMoK0Zjyjk-Y847lEYLyl4wjea" -O Nee_V2_ONNX/model.onnx

echo "Model size:"
ls -lh Nee_V2_ONNX/model.onnx

echo "Installing requirements..."
pip install --no-cache-dir -r requirements.txt

echo "Build completed."
