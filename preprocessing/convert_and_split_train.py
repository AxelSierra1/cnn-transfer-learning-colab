import os
import random
from PIL import Image
from tqdm import tqdm

random.seed(42)

# Configuration
INPUT_PATH = "C:/Users/vienn/OneDrive/Escritorio/NCT-CRC-HE-100K/NCT-CRC-HE-100K"
OUTPUT_PATH = "C:/Users/vienn/OneDrive/Escritorio/NCT-CRC-HE-100k-Binary"
CLASSES = {
    "malignant": ["TUM"],
    "benign": ["ADI", "BACK", "DEB", "LYM", "MUC", "MUS", "NORM", "STR"]
}
TRAIN_RATIO = 0.8

# Create output directories
for split in ["train", "val"]:
    for class_name in CLASSES:
        os.makedirs(os.path.join(OUTPUT_PATH, split, class_name), exist_ok=True)

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

        # Shuffle and split
        random.shuffle(images)
        split_idx = int(len(images) * TRAIN_RATIO)
        
        # Process both splits
        for split, subset in [("train", images[:split_idx]), 
                            ("val", images[split_idx:])]:
            print(f"\nProcessing {len(subset)} {class_name} images -> {split}")
            
            for img_path in tqdm(subset, desc=f"Converting {class_name}", unit="img"):
                # Convert to JPEG
                output_dir = os.path.join(OUTPUT_PATH, split, class_name)
                output_name = os.path.splitext(os.path.basename(img_path))[0] + ".jpg"
                
                with Image.open(img_path) as img:
                    img.convert("RGB").save(
                        os.path.join(output_dir, output_name),
                        "JPEG",
                        quality=95
                    )

process_dataset()
print("\n✅ All TIFFs converted to JPEG and split!")