import os
import shutil
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / 'staticfiles' / 'images'  # Changed to staticfiles
MEDIA_DIR = BASE_DIR / 'media'

# Create media directories
(MEDIA_DIR / 'hero').mkdir(parents=True, exist_ok=True)
(MEDIA_DIR / 'services').mkdir(parents=True, exist_ok=True)

# Copy hero service image
hero_service_src = STATIC_DIR / 'demo-images' / 'demo-digital-agency.jpg'
hero_service_dst = MEDIA_DIR / 'hero' / 'demo-digital-agency.jpg'
if hero_service_src.exists():
    shutil.copy2(hero_service_src, hero_service_dst)
    print(f'✓ Copied {hero_service_src.name} to hero/')
else:
    print(f'✗ Not found: {hero_service_src}')

# Service images mapping - using available demo images
service_images = {
    'demo-digital-agency.jpg': 'services/demo-digital-agency.jpg',  # Social Media Marketing
    'demo-corporate.jpg': 'services/demo-corporate.jpg',  # Branding
    'demo-freelancer.jpg': 'services/demo-freelancer.jpg',  # Website Development
    'demo-data-analysis.jpg': 'services/demo-data-analysis.jpg',  # SEO & Google Ads
    'demo-consulting.jpg': 'services/demo-consulting.jpg',  # Email Marketing
}

for img_name, dest_path in service_images.items():
    src = STATIC_DIR / 'demo-images' / img_name
    dst = MEDIA_DIR / dest_path
    if src.exists():
        shutil.copy2(src, dst)
        print(f'✓ Copied {img_name} to {dest_path}')
    else:
        print(f'✗ Not found: {src}')

print('\n✅ Service images copied successfully!')
