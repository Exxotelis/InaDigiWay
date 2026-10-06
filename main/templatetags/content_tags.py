from django import template
from django.utils.translation import get_language

register = template.Library()


@register.filter(name='in_current_lang')
def in_current_lang(obj, field_name):
	"""
	Template filter to get field value in current language.
	Usage: {{ hero|in_current_lang:"title_part1_line1" }}
	
	This will automatically fetch title_part1_line1_en or title_part1_line1_el
	based on the current language.
	"""
	if obj is None:
		return ""
	
	lang = get_language()
	
	# Determine language suffix
	if lang.startswith('el'):
		lang_suffix = '_el'
	else:
		lang_suffix = '_en'
	
	# Try to get the field with language suffix
	field_with_lang = f"{field_name}{lang_suffix}"
	value = getattr(obj, field_with_lang, None)
	
	# If not found or empty, fallback to English
	if not value:
		fallback_field = f"{field_name}_en"
		value = getattr(obj, fallback_field, "")
	
	return value


@register.filter(name='webp')
def webp(image_field, max_width=1000):
	"""
	Return the URL of a resized WebP copy of an uploaded image.
	Usage: <img src="{{ service.image|webp:900 }}">

	Copies are written once to MEDIA_ROOT/_opt/ and regenerated when the
	original changes (its mtime is part of the filename). Falls back to the
	original URL if anything goes wrong.
	"""
	import hashlib
	import os

	from django.conf import settings
	from PIL import Image, ImageOps

	try:
		src_path = image_field.path
		original_url = image_field.url
	except Exception:
		return ""

	try:
		max_width = int(max_width)
		mtime = int(os.path.getmtime(src_path))
		key = hashlib.md5(f"{image_field.name}:{mtime}".encode()).hexdigest()[:10]
		stem = os.path.splitext(os.path.basename(image_field.name))[0]
		out_name = f"{stem}-{max_width}-{key}.webp"
		out_dir = os.path.join(settings.MEDIA_ROOT, "_opt")
		out_path = os.path.join(out_dir, out_name)

		if not os.path.exists(out_path):
			os.makedirs(out_dir, exist_ok=True)
			with Image.open(src_path) as img:
				img = ImageOps.exif_transpose(img)
				if img.mode not in ("RGB", "RGBA"):
					img = img.convert("RGBA" if "transparency" in img.info or img.mode in ("LA", "P") else "RGB")
				if img.width > max_width:
					img.thumbnail((max_width, max_width * 10), Image.LANCZOS)
				tmp_path = out_path + ".tmp"
				img.save(tmp_path, "WEBP", quality=80, method=4)
				os.replace(tmp_path, out_path)

		return f"{settings.MEDIA_URL}_opt/{out_name}"
	except Exception:
		return original_url


@register.filter(name='webp_srcset')
def webp_srcset(image_field, widths="500,1000"):
	"""
	Build a srcset of resized WebP copies.
	Usage: srcset="{{ service.image|webp_srcset:'500,1000' }}"
	"""
	parts = []
	for w in str(widths).split(","):
		url = webp(image_field, w.strip())
		if url:
			parts.append(f"{url} {w.strip()}w")
	return ", ".join(parts)


@register.simple_tag(takes_context=True)
def local_business_jsonld(context, description="", page_url="https://inadigiway.com/"):
	"""
	schema.org LocalBusiness (ProfessionalService) JSON-LD for the <head>.
	Contact details and services come from the admin (Footer, Hero, Services),
	so the structured data always matches what visitors see on the page.
	Usage: {% local_business_jsonld seo_description page_url %}
	"""
	import json

	from django.templatetags.static import static
	from django.utils.safestring import mark_safe

	footer = context.get("footer")
	hero = context.get("hero")
	services = context.get("services") or []
	is_el = (get_language() or "").startswith("el")

	same_as = []
	if footer:
		for url in (footer.instagram_url, footer.facebook_url, footer.linkedin_url, footer.google_business_url):
			# Skip placeholder links such as a bare "https://linkedin.com"
			if url and url.rstrip("/").count("/") > 2:
				same_as.append(url)

	service_names = []
	if hero and in_current_lang(hero, "service_title"):
		service_names.append(in_current_lang(hero, "service_title"))
	service_names += [in_current_lang(s, "title") for s in services]

	data = {
		"@context": "https://schema.org",
		"@type": "ProfessionalService",
		"@id": "https://inadigiway.com/#business",
		"name": "InaDigiWay",
		"alternateName": "In A Digi Way",
		"url": page_url,
		"logo": "https://inadigiway.com" + static("images/logo.png"),
		"image": "https://inadigiway.com" + static("images/logo.png"),
		"description": description,
		"address": {
			"@type": "PostalAddress",
			"addressLocality": "Αθήνα" if is_el else "Athens",
			"addressCountry": "GR",
		},
		"areaServed": {"@type": "Country", "name": "Ελλάδα" if is_el else "Greece"},
		"founder": {"@type": "Person", "name": "Ina Lasko"},
		"knowsLanguage": ["el", "en"],
		"hasOfferCatalog": {
			"@type": "OfferCatalog",
			"name": "Υπηρεσίες" if is_el else "Services",
			"itemListElement": [
				{"@type": "Offer", "itemOffered": {"@type": "Service", "name": name}}
				for name in service_names
			],
		},
	}
	if footer:
		if footer.phone_number:
			data["telephone"] = footer.phone_number
		if footer.email_address:
			data["email"] = footer.email_address
	if same_as:
		data["sameAs"] = same_as
	if footer and footer.google_business_url:
		data["hasMap"] = footer.google_business_url

	payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
	return mark_safe(f'<script type="application/ld+json">\n{payload}\n</script>')
