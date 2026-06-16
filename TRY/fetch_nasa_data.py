import requests
import rasterio
from rasterio.plot import reshape_as_image
import numpy as np
from PIL import Image
import os

API_KEY = "sFq2tfJPmJIa4SWmOMAxogUbYscJqSYlggEnLH65"
DATA_DIR = "tiles"
os.makedirs(DATA_DIR, exist_ok=True)

# Example: MODIS LST daily tile URL (replace with actual tile URL)
MODIS_URL = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/your_file_id_here"

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(MODIS_URL, headers=headers)
local_hdf = os.path.join(DATA_DIR, "MODIS_tile.hdf")
with open(local_hdf, "wb") as f:
    f.write(response.content)

# Convert HDF/GeoTIFF to PNG for web
with rasterio.open(local_hdf) as src:
    data = src.read(1)  # read first band
    data = np.clip(data, 0, 400)  # clip LST range
    data = (data / data.max() * 255).astype(np.uint8)
    img = Image.fromarray(data)
    img.save(os.path.join(DATA_DIR, "MODIS_tile.png"))

print("MODIS tile PNG ready!")
