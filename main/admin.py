from django.contrib import admin

from .models import SiteSettings, AnalyticsSettings, Testimonial


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
	list_display = ("calendly_url", "updated_at")
	ordering = ("-updated_at",)

	def has_add_permission(self, request):
		return not SiteSettings.objects.exists()

	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(AnalyticsSettings)
class AnalyticsSettingsAdmin(admin.ModelAdmin):
	list_display = ("display_name", "ga4_measurement_id", "updated_at")
	list_display_links = ("display_name",)
	ordering = ("-updated_at",)

	@admin.display(description="Analytics Settings")
	def display_name(self, obj):
		return "Analytics Settings"

	def has_add_permission(self, request):
		return not AnalyticsSettings.objects.exists()

	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ("name", "company", "role", "is_active", "sort_order", "created_at")
	list_filter = ("is_active",)
	search_fields = ("name", "company", "role", "quote", "quote_en", "quote_el")
	ordering = ("sort_order", "-created_at")
	fieldsets = (
		("Client", {"fields": ("name", "role", "company")}),
		("Quote (English)", {"fields": ("quote_en",)}),
		("Quote (Greek)", {"fields": ("quote_el",)}),
		("Fallback", {"fields": ("quote",)}),
		("Display", {"fields": ("is_active", "sort_order")}),
	)
