"""
URL configuration for InaDigi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.http import Http404, HttpResponse

from main.views import home


def ads_txt(request):
    from main.models import SiteSettings

    settings_obj = SiteSettings.get_solo()
    client = settings_obj.adsense_client
    if not (settings_obj.adsense_enabled and client):
        raise Http404
    return HttpResponse(f"google.com, {client[3:]}, DIRECT, f08c47fec0942fa0\n", content_type="text/plain")


def robots_txt(request):
    return HttpResponse(
        "User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: https://inadigiway.com/sitemap.xml\n",
        content_type="text/plain",
    )


def sitemap_xml(request):
    # One page in two languages: Greek at /, English at /en/, linked with hreflang.
    alternates = (
        '    <xhtml:link rel="alternate" hreflang="el" href="https://inadigiway.com/"/>\n'
        '    <xhtml:link rel="alternate" hreflang="en" href="https://inadigiway.com/en/"/>\n'
        '    <xhtml:link rel="alternate" hreflang="x-default" href="https://inadigiway.com/"/>\n'
    )
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "".join(
            f"  <url>\n    <loc>{loc}</loc>\n{alternates}  </url>\n"
            for loc in ("https://inadigiway.com/", "https://inadigiway.com/en/")
        )
        + "</urlset>\n"
    )
    return HttpResponse(body, content_type="application/xml")


admin.site.site_header = "InaDigiWay"
admin.site.site_title = "InaDigiWay"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('ads.txt', ads_txt),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
]

# Greek (default) is served at / with no prefix, English at /en/.
urlpatterns += i18n_patterns(
    path('', home, name='home'),
    prefix_default_language=False,
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
