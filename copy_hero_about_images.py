import os
import shutil
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / 'static' / 'images'
MEDIA_DIR = BASE_DIR / 'media'

# Create media directories
(MEDIA_DIR / 'about').mkdir(parents=True, exist_ok=True)
(MEDIA_DIR / 'about' / 'badges').mkdir(parents=True, exist_ok=True)

# Copy about main image
about_main_src = STATIC_DIR / 'about' / 'ina-about.jpg'
about_main_dst = MEDIA_DIR / 'about' / 'ina-about.jpg'
if about_main_src.exists():
    shutil.copy2(about_main_src, about_main_dst)
    print(f'✓ Copied {about_main_src.name} to about/')
else:
    print(f'✗ Not found: {about_main_src}')

# Copy about badges
badge_images = [
    ('badge-1.png', 'about/badges/badge-1.png'),
    ('badge-2.png', 'about/badges/badge-2.png'),
    ('badge-3.png', 'about/badges/badge-3.png'),
]

for img_name, dest_path in badge_images:
    src = STATIC_DIR / 'about' / img_name
    dst = MEDIA_DIR / dest_path
    if src.exists():
        shutil.copy2(src, dst)
        print(f'✓ Copied {img_name} to {dest_path}')
    else:
        print(f'✗ Not found: {src}')

print('\n✅ Hero and About images copied successfully!')
