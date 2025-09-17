import requests
from PIL import Image
from io import BytesIO
import os

# -------------------------------
# Configuration
# -------------------------------
API_KEY = "sFq2tfJPmJIa4SWmOMAxogUbYscJqSYlggEnLH65"
DATA_DIR = "tiles"
os.makedirs(DATA_DIR, exist_ok=True)

# Example NASA LAADS PNG or GeoTIFF URLs (replace with actual files)
# For simplicity, we use URLs pointing directly to PNGs if available.
INSTRUMENTS = {
    "MODIS": "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_modis_png_file_here",
    "ASTER": "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_aster_png_file_here",
    "MISR": "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_misr_png_file_here",
    "CERES": "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_ceres_png_file_here",
    "MOPITT": "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_mopitt_png_file_here",
}

# -------------------------------
# Function: Download and save PNG
# -------------------------------
def download_and_save_png(url, local_path):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    print(f"Downloading {url} ...")
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise Exception(f"Failed to download: {r.status_code}")

    # Open image directly from bytes
    img = Image.open(BytesIO(r.content))
    img.save(local_path)
    print(f"Saved PNG to {local_path}")

# -------------------------------
# Main: Fetch all instruments
# -------------------------------
for instr, url in INSTRUMENTS.items():
    png_file = os.path.join(DATA_DIR, f"{instr}.png")
    download_and_save_png(url, png_file)
