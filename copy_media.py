import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def copy_media_files():
    source_dir = os.path.join(BASE_DIR, 'media', 'project_images')
    target_dir = os.path.join(BASE_DIR, 'staticfiles', 'media', 'project_images')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Copy all files from source to target
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        if os.path.isfile(source_item):
            shutil.copy2(source_item, target_item)
            print(f"Copied: {item}")

if __name__ == "__main__":
    copy_media_files()
    print("Media files copied successfully!")
