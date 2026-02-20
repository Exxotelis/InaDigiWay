import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import (
    HeroContent, Service, AboutContent, FooterContent, ClientLogo
)

def fix_all_content():
    print("🔧 Fixing all content to match original...")
    
    # Fix Hero
    hero, _ = HeroContent.objects.get_or_create(pk=1)
    hero.mega_text_en = "IDEAS THAT CONVERT!"
    hero.mega_text_el = "IDEAS THAT CONVERT!"
    hero.title_part1_line1_en = "A digital agency"
    hero.title_part1_line1_el = "Μια digital εταιρεία"
    hero.title_part1_line2_en = "focused on"
    hero.title_part1_line2_el = "που επικεντρώνεται στην"
    hero.title_part2_en = "GROWTH!"
    hero.title_part2_el = "ΑΝAΠΤΥΞΗ!"
    hero.service_image = 'services/social-media.jpg'
    hero.service_title_en = "SOCIAL MEDIA MARKETING"
    hero.service_title_el = "SOCIAL MEDIA MARKETING"
    hero.service_description_en = "When there's one great thing, there's usually another. What's your second thing to showcase?"
    hero.service_description_el = "Όταν υπάρχει ένα σπουδαίο πράγμα, συνήθως υπάρχει και ένα άλλο. Ποιο είναι το δεύτερο πράγμα που θέλεις να δείξεις;"
    hero.service_button_text_en = "VIEW INST ACC"
    hero.service_button_text_el = "ΔΕΙΤΕ ΤΟ INST"
    hero.service_button_url = "https://www.instagram.com/inadigiway"
    hero.save()
    print("✅ Hero fixed")
    
    # Delete all services and recreate
    Service.objects.all().delete()
    
    services_data = [
        {
            'title_en': 'INFLUENCER MARKETING',
            'title_el': 'INFLUENCER MARKETING',
            'description_en': 'Connect with the right influencers to amplify your message & reach new audiences authentically.',
            'description_el': 'Συνδεθείτε με τους σωστούς influencers για να ενισχύσετε το μήνυμά σας και να φτάσετε σε νέο κοινό αυθεντικά.',
            'image': 'services/influencer-marketing.jpg',
            'button_text_en': 'GET A QUOTE',
            'button_text_el': 'ΖΗΤΗΣΤΕ ΠΡΟΣΦΟΡΑ',
            'button_link': '#quote',
            'layout': 'right',
            'sort_order': 1,
        },
        {
            'title_en': 'EMAIL MARKETING',
            'title_el': 'EMAIL MARKETING',
            'description_en': 'Build lasting relationships with targeted email campaigns that convert subscribers into loyal customers.',
            'description_el': 'Δημιουργήστε μακροχρόνιες σχέσεις με στοχευμένες email καμπάνιες που μετατρέπουν τους συνδρομητές σε πιστούς πελάτες.',
            'image': 'services/email-marketing.jpg',
            'button_text_en': 'GET A QUOTE',
            'button_text_el': 'ΖΗΤΗΣΤΕ ΠΡΟΣΦΟΡΑ',
            'button_link': '#quote',
            'layout': 'left',
            'sort_order': 2,
        },
        {
            'title_en': 'CONTENT CREATION & MARKETING',
            'title_el': 'ΔΗΜΙΟΥΡΓΙΑ & MARKETING ΠΕΡΙΕΧΟΜΕΝΟΥ',
            'description_en': 'Compelling stories, stunning visuals & engaging copy that captivate your audience and drive results.',
            'description_el': 'Συναρπαστικές ιστορίες, εντυπωσιακά visuals και ελκυστικά κείμενα που αιχμαλωτίζουν το κοινό σας και φέρνουν αποτελέσματα.',
            'image': 'services/content-creation.jpg',
            'button_text_en': 'GET A QUOTE',
            'button_text_el': 'ΖΗΤΗΣΤΕ ΠΡΟΣΦΟΡΑ',
            'button_link': '#quote',
            'layout': 'right',
            'sort_order': 3,
        },
        {
            'title_en': 'WEB DEVELOPMENT',
            'title_el': 'ΑΝΑΠΤΥΞΗ ΙΣΤΟΣΕΛΙΔΩΝ',
            'description_en': 'Custom-built websites & web apps that are fast, secure, and designed for conversions.',
            'description_el': 'Ιστοσελίδες και web εφαρμογές φτιαγμένες στα μέτρα σας που είναι γρήγορες, ασφαλείς και σχεδιασμένες για conversions.',
            'image': 'services/web-development.jpg',
            'button_text_en': 'BOOK A CALL TODAY',
            'button_text_el': 'ΚΛΕIΣΤΕ ΡΑΝΤΕΒΟΥ ΣΗΜΕΡΑ',
            'button_link': '#book-call',
            'layout': 'left',
            'sort_order': 4,
        },
        {
            'title_en': 'BRANDING',
            'title_el': 'BRANDING',
            'description_en': 'Build a memorable brand identity that connects with your audience and stands out from the crowd.',
            'description_el': 'Δημιουργήστε μια αξέχαστη ταυτότητα brand που συνδέεται με το κοινό σας και ξεχωρίζει από το πλήθος.',
            'image': 'demo-images/demo-digital-agency.jpg',
            'button_text_en': 'BOOK A CALL TODAY',
            'button_text_el': 'ΚΛΕΙΣΤΕ ΡΑΝΤΕΒΟΥ ΣΗΜΕΡΑ',
            'button_link': '#book-call',
            'layout': 'right',
            'sort_order': 5,
        },
    ]
    
    for service_data in services_data:
        Service.objects.create(**service_data)
    print(f"✅ {len(services_data)} services created")
    
    # Fix About
    about, _ = AboutContent.objects.get_or_create(pk=1)
    about.main_image = 'InaDigi.jpg'
    about.badge_image_1 = 'about/41.png'
    about.badge_image_2 = 'about/74.png'
    about.badge_image_3 = 'about/35.png'
    about.save()
    print("✅ About images fixed")
    
    # Fix Footer
    footer, _ = FooterContent.objects.get_or_create(pk=1)
    footer.logo = 'ina-digi-way-margarita-pagouni-62.png'
    footer.qr_code = 'InaQR.png'
    footer.save()
    print("✅ Footer images fixed")
    
    # Fix Client Logos
    ClientLogo.objects.all().delete()
    
    logos = [
        ('VV-logo.png', 'VV Logo'),
        ('spotify.png', 'Spotify'),
        ('youtube.png', 'YouTube'),
        ('telegram.png', 'Telegram'),
        ('tiktok.png', 'TikTok'),
        ('snapchat.png', 'Snapchat'),
        ('search.png', 'Search'),
        ('profile-img.png', 'Profile'),
        ('02.png', 'Brand Logo'),
    ]
    
    for idx, (filename, name) in enumerate(logos, 1):
        ClientLogo.objects.create(
            name=name,
            logo=f'client-logos/{filename}',
            is_active=True,
            sort_order=idx
        )
    print(f"✅ {len(logos)} client logos created")
    
    print("\n✨ All content fixed to match original!")

if __name__ == '__main__':
    fix_all_content()
