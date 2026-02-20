import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import ServicesContent, AboutContent, ContactContent, HappyClientsContent

print('=== Seeding Services Content ===')
services_content, created = ServicesContent.objects.get_or_create(id=1)
services_content.mega_text_en = 'IDEAS THAT CONVERT!'
services_content.mega_text_el = 'ΙΔΕΕΣ ΠΟΥ ΜΕΤΑΤΡΕΠΟΝΤΑΙ!'
services_content.save()
print(f'✓ {"Created" if created else "Updated"} services content')

print('\n=== Seeding About Content ===')
about, created = AboutContent.objects.get_or_create(id=1)
about.title_en = "Who's behind the Digi?"
about.title_el = 'Ποιος κρύβεται πίσω από το Digi;'
about.intro_name_en = 'Ina Lasko - a digital creative,'
about.intro_name_el = 'Η Ίνα Λάσκο - μια ψηφιακή δημιουργός,'
about.intro_text_en = 'based in Athens with a passion for brands that want to stand out!'
about.intro_text_el = 'που εδρεύει στην Αθήνα με πάθος για brands που θέλουν να ξεχωρίσουν!'
about.description_part1_en = 'Through'
about.description_part1_el = 'Μέσα από το'
about.brand_name_en = 'In A Digi Way,'
about.brand_name_el = 'In A Digi Way,'
about.description_part2_en = 'she combines strategic marketing with refined aesthetics, to give your social media, email campaigns and content a touch of... digital magic!'
about.description_part2_el = 'συνδυάζει το στρατηγικό μάρκετινγκ με εκλεπτυσμένη αισθητική, για να δώσει στα social media, τις email καμπάνιες και το περιεχόμενό σας μια πινελιά... ψηφιακής μαγείας!'
about.button_text_en = 'BOOK A CALL TODAY'
about.button_text_el = 'ΚΛΕΙΣΕ ΡΑΝΤΕΒΟΥ ΣΗΜΕΡΑ'
about.button_link = '#book-call'
about.save()
print(f'✓ {"Created" if created else "Updated"} about content')

print('\n=== Seeding Contact Content ===')
contact, created = ContactContent.objects.get_or_create(id=1)
contact.title_en = 'CONTACT FORM'
contact.title_el = 'ΦΟΡΜΑ ΕΠΙΚΟΙΝΩΝΙΑΣ'
contact.happy_clients_title_en = 'HAPPY CLIENTS'
contact.happy_clients_title_el = 'ΕΥΧΑΡΙΣΤΗΜΕΝΟΙ ΠΕΛΑΤΕΣ'
contact.label_name_en = 'Name'
contact.label_name_el = 'Όνομα'
contact.label_phone_en = 'Phone'
contact.label_phone_el = 'Τηλέφωνο'
contact.label_email_en = 'E-mail'
contact.label_email_el = 'E-mail'
contact.label_service_en = 'Service'
contact.label_service_el = 'Υπηρεσία'
contact.label_budget_en = 'Budget'
contact.label_budget_el = 'Προϋπολογισμός'
contact.label_message_en = 'Message'
contact.label_message_el = 'Μήνυμα'
contact.button_submit_en = 'SUBMIT'
contact.button_submit_el = 'ΥΠΟΒΟΛΗ'
contact.service_select_en = 'Select a service'
contact.service_select_el = 'Επιλέξτε υπηρεσία'
contact.budget_select_en = 'Select budget'
contact.budget_select_el = 'Επιλέξτε προϋπολογισμό'
contact.save()
print(f'✓ {"Created" if created else "Updated"} contact content')

print('\n=== Seeding Happy Clients Content ===')
happy_clients, created = HappyClientsContent.objects.get_or_create(id=1)
happy_clients.title_en = 'HAPPY CLIENTS'
happy_clients.title_el = 'ΕΥΧΑΡΙΣΤΗΜΕΝΟΙ ΠΕΛΑΤΕΣ'
happy_clients.placeholder_text_en = 'Client testimonials coming soon...'
happy_clients.placeholder_text_el = 'Οι μαρτυρίες πελατών έρχονται σύντομα...'
happy_clients.save()
print(f'✓ {"Created" if created else "Updated"} happy clients content')

print('\n✅ Successfully seeded all additional content!')
