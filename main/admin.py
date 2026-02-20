from django.contrib import admin
from django.utils.html import format_html

from .models import (
	SiteSettings, AnalyticsSettings, Testimonial, QuoteRequest,
	HeroContent, Service, ServicesContent, AboutContent, ContactContent,
	HappyClientsContent, FooterContent, ClientLogo
)


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


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone", "service", "budget", "created_at")
	search_fields = ("name", "email", "service", "message")
	readonly_fields = ("created_at",)


# ==================== CONTENT MANAGEMENT ====================

@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at", "service_image_preview")
	
	fieldsets = (
		("🎯 Mega Text (Vertical)", {
			"fields": (("mega_text_en", "mega_text_el"),)
		}),
		("💫 Main Title - Part 1", {
			"fields": (
				("title_part1_line1_en", "title_part1_line1_el"),
				("title_part1_line2_en", "title_part1_line2_el"),
			)
		}),
		("✨ Main Title - Part 2 (Highlight)", {
			"fields": (("title_part2_en", "title_part2_el"),)
		}),
		("🎴 Service Showcase Card", {
			"fields": (
				("service_title_en", "service_title_el"),
				("service_description_en", "service_description_el"),
				("service_button_text_en", "service_button_text_el"),
				"service_button_url",
				"service_image",
				"service_image_preview",
			)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def service_image_preview(self, obj):
		if obj.service_image:
			return format_html('<img src="{}" style="max-height: 200px; max-width: 300px;" />', obj.service_image.url)
		return "No image"
	service_image_preview.short_description = "Service Image Preview"
	
	def has_add_permission(self, request):
		return not HeroContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ("title_en", "layout", "sort_order", "is_active", "image_preview_thumbnail")
	list_filter = ("is_active", "layout")
	search_fields = ("title_en", "title_el", "description_en", "description_el")
	ordering = ("sort_order", "-created_at")
	readonly_fields = ("image_preview", "created_at", "updated_at")
	
	fieldsets = (
		("📝 Content", {
			"fields": (
				("title_en", "title_el"),
				("description_en", "description_el"),
			)
		}),
		("🖼️ Image & Layout", {
			"fields": (
				"image",
				"image_preview",
				"layout",
			)
		}),
		("🔘 Button", {
			"fields": (
				("button_text_en", "button_text_el"),
				"button_link",
			)
		}),
		("⚙️ Settings", {
			"fields": (
				"sort_order",
				"is_active",
			)
		}),
		("🕒 Metadata", {
			"fields": ("created_at", "updated_at"),
			"classes": ("collapse",)
		}),
	)
	
	def image_preview(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="max-height: 300px; max-width: 400px;" />', obj.image.url)
		return "No image"
	image_preview.short_description = "Image Preview"
	
	def image_preview_thumbnail(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="height: 50px; width: auto;" />', obj.image.url)
		return "❌"
	image_preview_thumbnail.short_description = "Image"


@admin.register(ServicesContent)
class ServicesContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at",)
	
	fieldsets = (
		("🎯 Mega Text (Vertical)", {
			"fields": (("mega_text_en", "mega_text_el"),)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def has_add_permission(self, request):
		return not ServicesContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at", "main_image_preview", "badge_top_left_preview", "badge_bottom_left_preview", "badge_bottom_right_preview")
	
	fieldsets = (
		("📌 Section Title", {
			"fields": (("title_en", "title_el"),)
		}),
		("👤 Introduction", {
			"fields": (
				("intro_name_en", "intro_name_el"),
				("intro_text_en", "intro_text_el"),
			)
		}),
		("📄 Description", {
			"fields": (
				("description_part1_en", "description_part1_el"),
				("brand_name_en", "brand_name_el"),
				("description_part2_en", "description_part2_el"),
			)
		}),
		("🔘 Call-to-Action Button", {
			"fields": (
				("button_text_en", "button_text_el"),
				"button_link",
			)
		}),
		("🖼️ Images", {
			"fields": (
				"main_image",
				"main_image_preview",
				"badge_top_left",
				"badge_top_left_preview",
				"badge_bottom_left",
				"badge_bottom_left_preview",
				"badge_bottom_right",
				"badge_bottom_right_preview",
			)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def main_image_preview(self, obj):
		if obj.main_image:
			return format_html('<img src="{}" style="max-height: 300px; max-width: 400px;" />', obj.main_image.url)
		return "No image"
	main_image_preview.short_description = "Main Image Preview"
	
	def badge_top_left_preview(self, obj):
		if obj.badge_top_left:
			return format_html('<img src="{}" style="max-height: 150px;" />', obj.badge_top_left.url)
		return "No image"
	badge_top_left_preview.short_description = "Badge Preview"
	
	def badge_bottom_left_preview(self, obj):
		if obj.badge_bottom_left:
			return format_html('<img src="{}" style="max-height: 150px;" />', obj.badge_bottom_left.url)
		return "No image"
	badge_bottom_left_preview.short_description = "Badge Preview"
	
	def badge_bottom_right_preview(self, obj):
		if obj.badge_bottom_right:
			return format_html('<img src="{}" style="max-height: 150px;" />', obj.badge_bottom_right.url)
		return "No image"
	badge_bottom_right_preview.short_description = "Badge Preview"
	
	def has_add_permission(self, request):
		return not AboutContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at",)
	
	fieldsets = (
		("📌 Section Titles", {
			"fields": (
				("title_en", "title_el"),
				("happy_clients_title_en", "happy_clients_title_el"),
			)
		}),
		("🏷️ Form Labels", {
			"fields": (
				("label_name_en", "label_name_el"),
				("label_phone_en", "label_phone_el"),
				("label_email_en", "label_email_el"),
				("label_service_en", "label_service_el"),
				("label_budget_en", "label_budget_el"),
				("label_message_en", "label_message_el"),
			)
		}),
		("📋 Dropdown Placeholders", {
			"fields": (
				("service_select_en", "service_select_el"),
				("budget_select_en", "budget_select_el"),
			)
		}),
		("🔘 Button", {
			"fields": (("button_submit_en", "button_submit_el"),)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def has_add_permission(self, request):
		return not ContactContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(HappyClientsContent)
class HappyClientsContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at",)
	
	fieldsets = (
		("📌 Content", {
			"fields": (
				("title_en", "title_el"),
				("placeholder_text_en", "placeholder_text_el"),
			)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def has_add_permission(self, request):
		return not HappyClientsContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(FooterContent)
class FooterContentAdmin(admin.ModelAdmin):
	list_display = ("__str__", "updated_at")
	readonly_fields = ("updated_at", "logo_preview", "qr_code_preview")
	
	fieldsets = (
		("🖼️ Logo", {
			"fields": (
				"logo_image",
				"logo_preview",
			)
		}),
		("🌐 Social Media", {
			"fields": (
				"instagram_url",
				"facebook_url",
				"linkedin_url",
			)
		}),
		("📞 Contact Info", {
			"fields": (
				("phone_label_en", "phone_label_el"),
				"phone_number",
				("email_label_en", "email_label_el"),
				"email_address",
			)
		}),
		("📱 QR Code", {
			"fields": (
				"qr_code_image",
				"qr_code_preview",
			)
		}),
		("©️ Copyright", {
			"fields": (
				"copyright_year",
				("copyright_text_en", "copyright_text_el"),
			)
		}),
		("🕒 Metadata", {
			"fields": ("updated_at",),
			"classes": ("collapse",)
		}),
	)
	
	def logo_preview(self, obj):
		if obj.logo_image:
			return format_html('<img src="{}" style="max-height: 150px;" />', obj.logo_image.url)
		return "No image"
	logo_preview.short_description = "Logo Preview"
	
	def qr_code_preview(self, obj):
		if obj.qr_code_image:
			return format_html('<img src="{}" style="max-height: 200px;" />', obj.qr_code_image.url)
		return "No image"
	qr_code_preview.short_description = "QR Code Preview"
	
	def has_add_permission(self, request):
		return not FooterContent.objects.exists()
	
	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
	list_display = ("name", "logo_preview_thumbnail", "sort_order", "is_active")
	list_filter = ("is_active",)
	search_fields = ("name",)
	ordering = ("sort_order", "name")
	readonly_fields = ("logo_preview", "created_at", "updated_at")
	
	fieldsets = (
		("📝 Client Info", {
			"fields": ("name",)
		}),
		("🖼️ Logo", {
			"fields": (
				"logo",
				"logo_preview",
			)
		}),
		("⚙️ Settings", {
			"fields": (
				"sort_order",
				"is_active",
			)
		}),
		("🕒 Metadata", {
			"fields": ("created_at", "updated_at"),
			"classes": ("collapse",)
		}),
	)
	
	def logo_preview(self, obj):
		if obj.logo:
			return format_html('<img src="{}" style="max-height: 200px; max-width: 300px;" />', obj.logo.url)
		return "No image"
	logo_preview.short_description = "Logo Preview"
	
	def logo_preview_thumbnail(self, obj):
		if obj.logo:
			return format_html('<img src="{}" style="height: 40px; width: auto;" />', obj.logo.url)
		return "❌"
	logo_preview_thumbnail.short_description = "Logo"
