import os
import io
import zipfile
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEE_V2_DIR = os.path.join(BASE_DIR, "Nee_V2")
os.makedirs(NEE_V2_DIR, exist_ok=True)

# Your new tokenizer ZIP / file ID
FILE_ID = "12F5s4htEf4OGSa4CoCG3r1m5H9jSlPGG"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

print("Downloading from Google Drive:", FILE_ID)
response = requests.get(URL)
response.raise_for_status()
data = response.content

# Try to extract as ZIP
try:
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        print("ZIP detected. Extracting...")
        z.extractall(NEE_V2_DIR)
        print("✓ Extracted ZIP contents into Nee_V2/")
except zipfile.BadZipFile:
    # Not ZIP → treat as tokenizer.json
    file_path = os.path.join(NEE_V2_DIR, "tokenizer.json")
    with open(file_path, "wb") as f:
        f.write(data)
    print("✓ Saved single file as tokenizer.json")

print("Tokenizer download + extraction complete.")
