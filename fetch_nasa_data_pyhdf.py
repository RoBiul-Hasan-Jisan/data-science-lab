import requests
from pyhdf.SD import SD, SDC
import numpy as np
from PIL import Image
import os

# -------------------------------
# Configuration
# -------------------------------
API_KEY = "sFq2tfJPmJIa4SWmOMAxogUbYscJqSYlggEnLH65"
DATA_DIR = "tiles"
os.makedirs(DATA_DIR, exist_ok=True)

# Example MODIS HDF URL (replace with actual NASA LAADS URL)
MODIS_HDF_URL = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_modis_file_id_here"

# Local file paths
local_hdf = os.path.join(DATA_DIR, "MODIS_tile.hdf")
local_png = os.path.join(DATA_DIR, "MODIS_tile.png")

# -------------------------------
# Step 1: Fetch HDF from NASA API
# -------------------------------
headers = {"Authorization": f"Bearer {API_KEY}"}
print("Downloading MODIS HDF tile...")
response = requests.get(MODIS_HDF_URL, headers=headers)
if response.status_code != 200:
    raise Exception(f"Failed to download: {response.status_code}")
with open(local_hdf, "wb") as f:
    f.write(response.content)
print(f"Saved HDF to {local_hdf}")

# -------------------------------
# Step 2: Read HDF with pyhdf
# -------------------------------
print("Reading HDF file with pyhdf...")
hdf = SD(local_hdf, SDC.READ)

# List all datasets in HDF
print("Available datasets:", hdf.datasets().keys())

# Replace 'LST_Day_1km' with the dataset you want from HDF
dataset_name = 'LST_Day_1km'
if dataset_name not in hdf.datasets():
    raise Exception(f"Dataset '{dataset_name}' not found in HDF file")

lst_dataset = hdf.select(dataset_name)
data = lst_dataset[:].astype(np.float32)

# -------------------------------
# Step 3: Normalize & Convert to PNG
# -------------------------------
print("Normalizing data and converting to PNG...")
# Clip values (e.g., 0-400 for LST)
data = np.clip(data, 0, 400)
# Normalize to 0-255
data = (data / data.max() * 255).astype(np.uint8)

# Create image and save
img = Image.fromarray(data)
img.save(local_png)
print(f"Saved PNG to {local_png}")
