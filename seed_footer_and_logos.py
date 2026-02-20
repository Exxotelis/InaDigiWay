import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import FooterContent, ClientLogo

print('=== Seeding Footer Content ===')
# Create or update footer content (without images for now)
footer, created = FooterContent.objects.get_or_create(id=1)
footer.instagram_url = 'https://www.instagram.com/inadigiway'
footer.facebook_url = 'https://www.facebook.com/61575931331769'
footer.linkedin_url = 'https://linkedin.com'
footer.phone_label_en = 'P.'
footer.phone_label_el = 'Τ.'
footer.phone_number = '+30 697 1907 299'
footer.email_label_en = 'E.'
footer.email_label_el = 'E.'
footer.email_address = 'info@inadigiway.com'
footer.copyright_text_en = 'In A Digi Way. All rights reserved.'
footer.copyright_text_el = 'In A Digi Way. Με την επιφύλαξη κάθε δικαιώματος.'
footer.copyright_year = 2026
footer.save()
print(f'✓ {"Created" if created else "Updated"} footer content')

print('\n✅ Successfully seeded footer content!')
print('\n⚠️ Note: Please upload footer logo, QR code, and client logos manually through the Django admin.')

