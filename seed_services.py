import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InaDigi.settings')
django.setup()

from main.models import Service

# Clear existing services
Service.objects.all().delete()

# Service data
services_data = [
    {
        'title_en': 'SOCIAL MEDIA MARKETING',
        'title_el': 'ΜΑΡΚΕΤΙΝΓΚ ΚΟΙΝΩΝΙΚΩΝ ΜΕΣΩΝ',
        'description_en': 'Strategic social media campaigns that engage your audience and drive results. From content creation to community management, we help your brand shine across all platforms.',
        'description_el': 'Στρατηγικές καμπάνιες social media που προσελκύουν το κοινό σας και φέρνουν αποτελέσματα. Από τη δημιουργία περιεχομένου έως τη διαχείριση της κοινότητας, βοηθάμε το brand σας να λάμψει σε όλες τις πλατφόρμες.',
        'image': 'services/demo-digital-agency.jpg',
        'layout': 'right',
        'sort_order': 1,
    },
    {
        'title_en': 'BRANDING & IDENTITY',
        'title_el': 'BRANDING & ΤΑΥΤΟΤΗΤΑ',
        'description_en': 'Build a memorable brand identity that resonates with your target audience. We create cohesive visual identities, from logos to brand guidelines.',
        'description_el': 'Δημιουργήστε μια αξέχαστη ταυτότητα brand που αντηχεί στο κοινό-στόχο σας. Δημιουργούμε συνεκτικές οπτικές ταυτότητες, από logos έως brand guidelines.',
        'image': 'services/demo-corporate.jpg',
        'layout': 'left',
        'sort_order': 2,
    },
    {
        'title_en': 'WEBSITE DEVELOPMENT',
        'title_el': 'ΑΝΑΠΤΥΞΗ ΙΣΤΟΣΕΛΙΔΩΝ',
        'description_en': 'Beautiful, responsive websites that convert visitors into customers. We combine cutting-edge design with powerful functionality.',
        'description_el': 'Όμορφες, responsive ιστοσελίδες που μετατρέπουν τους επισκέπτες σε πελάτες. Συνδυάζουμε το σύγχρονο design με ισχυρή λειτουργικότητα.',
        'image': 'services/demo-freelancer.jpg',
        'layout': 'right',
        'sort_order': 3,
    },
    {
        'title_en': 'SEO & GOOGLE ADS',
        'title_el': 'SEO & ΔΙΑΦΗΜΙΣΕΙΣ GOOGLE',
        'description_en': 'Get found online with our SEO expertise and targeted Google Ads campaigns. Drive qualified traffic and maximize your ROI.',
        'description_el': 'Βρεθείτε online με την εμπειρία μας στο SEO και στοχευμένες καμπάνιες Google Ads. Προσελκύστε ποιοτική επισκεψιμότητα και μεγιστοποιήστε το ROI σας.',
        'image': 'services/demo-data-analysis.jpg',
        'layout': 'left',
        'sort_order': 4,
    },
    {
        'title_en': 'EMAIL MARKETING',
        'title_el': 'EMAIL MARKETING',
        'description_en': 'Engage your audience with personalized email campaigns that deliver results. From newsletters to automated sequences, we craft emails that convert.',
        'description_el': 'Προσελκύστε το κοινό σας με εξατομικευμένες email καμπάνιες που φέρνουν αποτελέσματα. Από newsletters έως αυτοματοποιημένες ακολουθίες, δημιουργούμε emails που μετατρέπουν.',
        'image': 'services/demo-consulting.jpg',
        'layout': 'right',
        'sort_order': 5,
    },
]

# Create services
for data in services_data:
    service = Service.objects.create(**data)
    print(f'✓ Created service: {service.title_en}')

print(f'\n✅ Successfully seeded {Service.objects.count()} services!')
