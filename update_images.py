import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import (
    HeroContent, Service, AboutContent, FooterContent, ClientLogo
)

def update_images():
    print("🖼️  Updating image paths in database...")
    
    # Update Hero
    try:
        hero = HeroContent.objects.first()
        if hero:
            hero.logo = 'hero/logo.png'
            hero.service_image = None  # The hero doesn't need service_image
            hero.save()
            print("✅ Hero logo updated")
    except Exception as e:
        print(f"⚠️  Hero: {e}")
    
    # Update About
    try:
        about = AboutContent.objects.first()
        if about:
            about.main_image = 'about/35.png'
            about.badge_image_1 = 'about/41.png'
            about.badge_image_2 = 'about/74.png'
            about.badge_image_3 = None  # We don't have a 4th image
            about.save()
            print("✅ About images updated")
    except Exception as e:
        print(f"⚠️  About: {e}")
    
    # Update Footer
    try:
        footer = FooterContent.objects.first()
        if footer:
            footer.logo = 'footer/logo.png'
            footer.qr_code = 'footer/InaQR.png'
            footer.save()
            print("✅ Footer images updated")
    except Exception as e:
        print(f"⚠️  Footer: {e}")
    
    # Update Services with the correct image names
    service_images = {
        'Branding': 'services/branding.jpg',
        'Content Creation': 'services/content-creation.jpg',
        'Email Marketing': 'services/email-marketing.jpg',
        'Influencer Marketing': 'services/influencer-marketing.jpg',
        'Social Media Management': 'services/social-media.jpg',
    }
    
    for service_name_en, image_path in service_images.items():
        try:
            service = Service.objects.filter(title_en__icontains=service_name_en.split()[0]).first()
            if service:
                service.image = image_path
                service.save()
                print(f"✅ {service_name_en} image updated")
        except Exception as e:
            print(f"⚠️  {service_name_en}: {e}")
    
    # Delete existing client logos and create new ones
    ClientLogo.objects.all().delete()
    
    logo_files = [
        ('02.png', 'Client Logo 1'),
        ('snapchat.png', 'Snapchat'),
        ('spotify.png', 'Spotify'),
        ('telegram.png', 'Telegram'),
        ('tiktok.png', 'TikTok'),
        ('youtube.png', 'YouTube'),
    ]
    
    for filename, name in logo_files:
        try:
            ClientLogo.objects.create(
                name=name,
                logo=f'client-logos/{filename}',
                is_active=True,
                sort_order=logo_files.index((filename, name)) + 1
            )
            print(f"✅ Client logo {name} created")
        except Exception as e:
            print(f"⚠️  {name}: {e}")
    
    print("\n✨ All images updated successfully!")

if __name__ == '__main__':
    update_images()
