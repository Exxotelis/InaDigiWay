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
