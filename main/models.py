from django.db import models


class SiteSettings(models.Model):
	calendly_url = models.URLField(blank=True, default="")
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return "Site Settings"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.exclude(calendly_url="").order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class AnalyticsSettings(models.Model):
	ga4_measurement_id = models.CharField(max_length=32, blank=True, default="")
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return "Analytics Settings"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class Testimonial(models.Model):
	name = models.CharField(max_length=120)
	role = models.CharField(max_length=120, blank=True, default="")
	company = models.CharField(max_length=120, blank=True, default="")
	quote_en = models.TextField(blank=True, default="")
	quote_el = models.TextField(blank=True, default="")
	quote = models.TextField(blank=True, default="")
	sort_order = models.PositiveIntegerField(default=0)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ("sort_order", "-created_at")

	def __str__(self) -> str:
		return f"{self.name}"


class QuoteRequest(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=40, blank=True, default="")
	service = models.CharField(max_length=200, blank=True, default="")
	budget = models.CharField(max_length=100, blank=True, default="")
	message = models.TextField(blank=True, default="")
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ("-created_at",)

	def __str__(self) -> str:
		return f"QuoteRequest from {self.name} <{self.email}>"
