import os
from PIL import Image
from tqdm import tqdm

# Configuration
INPUT_PATH = "C:/Users/vienn/OneDrive/Escritorio/CRC-VAL-HE-7K/CRC-VAL-HE-7K"
OUTPUT_PATH = "C:/Users/vienn/OneDrive/Escritorio/CRC-VAL-HE-7k-Binary"
CLASSES = {
    "malignant": ["TUM"],
    "benign": ["ADI", "BACK", "DEB", "LYM", "MUC", "MUS", "NORM", "STR"]
}

# Create output directories
for class_name in CLASSES:
    os.makedirs(os.path.join(OUTPUT_PATH, "test", class_name), exist_ok=True)

def process_dataset():
    for class_name, categories in CLASSES.items():
        # Collect all .tif images
        images = []
        for category in categories:
            folder = os.path.join(INPUT_PATH, category)
            images.extend([
                os.path.join(folder, f) 
                for f in os.listdir(folder) 
                if f.endswith(".tif")
            ])

        print(f"\nProcessing {len(images)} {class_name} images")
        
        for img_path in tqdm(images, desc=f"Converting {class_name}", unit="img"):
            # Convert to JPEG
            output_dir = os.path.join(OUTPUT_PATH, "test", class_name)
            output_name = os.path.splitext(os.path.basename(img_path))[0] + ".jpg"
            
            with Image.open(img_path) as img:
                img.convert("RGB").save(
                    os.path.join(output_dir, output_name),
                    "JPEG",
                    quality=95
                )

process_dataset()
print("\n✅ All TIFFs converted to JPEG and classified!")