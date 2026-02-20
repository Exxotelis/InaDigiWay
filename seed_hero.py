import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import HeroContent

print('=== Seeding Hero Content ===')
# Create or update hero content
hero, created = HeroContent.objects.get_or_create(id=1)
hero.mega_text_en = 'IDEAS THAT CONVERT!'
hero.mega_text_el = 'ΙΔΕΕΣ ΠΟΥ ΜΕΤΑΤΡΕΠΟΝΤΑΙ!'
hero.title_part1_line1_en = 'A digital agency'
hero.title_part1_line1_el = 'Ένα ψηφιακό πρακτορείο'
hero.title_part1_line2_en = 'focused on'
hero.title_part1_line2_el = 'που επικεντρώνεται στην'
hero.title_part2_en = 'GROWTH!'
hero.title_part2_el = 'ΑΝΑΠΤΥΞΗ!'
hero.service_title_en = 'SOCIAL MEDIA MARKETING'
hero.service_title_el = 'ΜΑΡΚΕΤΙΝΓΚ ΚΟΙΝΩΝΙΚΩΝ ΜΕΣΩΝ'
hero.service_description_en = 'Strategic social media campaigns that engage your audience and drive results. From content creation to community management.'
hero.service_description_el = 'Στρατηγικές καμπάνιες social media που προσελκύουν το κοινό σας και φέρνουν αποτελέσματα. Από τη δημιουργία περιεχομένου έως τη διαχείριση της κοινότητας.'
hero.service_button_text_en = 'VIEW INST ACC'
hero.service_button_text_el = 'ΔΕΙΤΕ ΤΟ INST'
hero.service_button_url = 'https://www.instagram.com/inadigiway'
hero.service_image = 'hero/demo-digital-agency.jpg'
hero.save()
print(f'✓ {"Created" if created else "Updated"} hero content')

print('\n✅ Successfully seeded hero content!')
