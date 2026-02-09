from .models import SiteSettings, AnalyticsSettings, Testimonial


def site_settings(request):
    settings = SiteSettings.get_solo()
    analytics = AnalyticsSettings.get_solo()
    testimonials = Testimonial.objects.filter(is_active=True)
    return {
        "site_settings": settings,
        "calendly_url": settings.calendly_url,
        "ga4_measurement_id": analytics.ga4_measurement_id,
        "testimonials": testimonials,
    }
