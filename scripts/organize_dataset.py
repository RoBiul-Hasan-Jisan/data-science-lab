import os
import shutil

# === CONFIGURATION ===
source_dir = r"D:\ml_lern\sample_fewShot"
target_dir = r"D:\ml_lern\sample_fewShot_processed"

# === CREATE TARGET DIRECTORY IF NOT EXISTS ===
os.makedirs(target_dir, exist_ok=True)

# === LOOP OVER IMAGES ===
for filename in os.listdir(source_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        # Extract class name from filename prefix before underscore
        if "_" in filename:
            label = filename.split("_")[0]
        else:
            print(f"⚠️ Skipped (no label in name): {filename}")
            continue

        # Create class folder
        label_folder = os.path.join(target_dir, label)
        os.makedirs(label_folder, exist_ok=True)

        # Define source and destination paths
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(label_folder, filename)

        # Copy image to new class folder
        shutil.copy2(src_path, dst_path)

print("✅ Dataset organized successfully!")
print(f"Organized images are in: {target_dir}")
