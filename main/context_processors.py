from .models import (
	SiteSettings, AnalyticsSettings, Testimonial,
	HeroContent, Service, ServicesContent, AboutContent, ContactContent,
	HappyClientsContent, FooterContent, ClientLogo
)


def site_settings(request):
    settings = SiteSettings.get_solo()
    analytics = AnalyticsSettings.get_solo()
    testimonials = Testimonial.objects.filter(is_active=True)
    
    # Content management models
    hero = HeroContent.get_solo()
    services = Service.objects.filter(is_active=True)
    services_content = ServicesContent.get_solo()
    about = AboutContent.get_solo()
    contact_content = ContactContent.get_solo()
    happy_clients_content = HappyClientsContent.get_solo()
    footer = FooterContent.get_solo()
    client_logos = ClientLogo.objects.filter(is_active=True)
    
    return {
        "site_settings": settings,
        "calendly_url": settings.calendly_url,
        "ga4_measurement_id": analytics.ga4_measurement_id,
        "testimonials": testimonials,
        # Content management
        "hero": hero,
        "services": services,
        "services_content": services_content,
        "about": about,
        "contact_content": contact_content,
        "happy_clients_content": happy_clients_content,
        "footer": footer,
        "client_logos": client_logos,
    }
