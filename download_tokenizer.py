import requests, zipfile, io, os

# Google Drive direct download link (from your ZIP)
URL = "https://drive.google.com/uc?export=download&id=127Ic7Zf1HC6NZ5CbVTfUo5EWgcbRzy09"

print("Downloading tokenizer ZIP from Google Drive...")
response = requests.get(URL)
response.raise_for_status()

print("Extracting ZIP...")
z = zipfile.ZipFile(io.BytesIO(response.content))

os.makedirs("Nee_V2", exist_ok=True)
z.extractall("Nee_V2")

print("Tokenizer successfully extracted into Nee_V2/")
