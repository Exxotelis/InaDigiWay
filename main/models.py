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


class HeroContent(models.Model):
	"""Hero section content - singleton model"""
	# Mega text (left and right vertical text)
	mega_text_en = models.CharField(max_length=200, default="IDEAS THAT CONVERT!", verbose_name="Mega Text (English)")
	mega_text_el = models.CharField(max_length=200, default="ΙΔΕΕΣ ΠΟΥ ΜΕΤΑΤΡΕΠΟΝΤΑΙ!", verbose_name="Mega Text (Greek)")
	
	# Main title - Part 1 (normal text)
	title_part1_line1_en = models.CharField(max_length=100, default="A digital agency", verbose_name="Title Part 1 - Line 1 (EN)")
	title_part1_line1_el = models.CharField(max_length=100, default="Ένα ψηφιακό πρακτορείο", verbose_name="Title Part 1 - Line 1 (EL)")
	title_part1_line2_en = models.CharField(max_length=100, default="focused on", verbose_name="Title Part 1 - Line 2 (EN)")
	title_part1_line2_el = models.CharField(max_length=100, default="που επικεντρώνεται στην", verbose_name="Title Part 1 - Line 2 (EL)")
	
	# Main title - Part 2 (highlighted text)
	title_part2_en = models.CharField(max_length=100, default="GROWTH!", verbose_name="Title Part 2 - Highlight (EN)")
	title_part2_el = models.CharField(max_length=100, default="ΑΝΑΠΤΥΞΗ!", verbose_name="Title Part 2 - Highlight (EL)")
	
	# Service showcase card
	service_title_en = models.CharField(max_length=200, default="SOCIAL MEDIA MARKETING", verbose_name="Service Title (EN)")
	service_title_el = models.CharField(max_length=200, default="ΜΑΡΚΕΤΙΝΓΚ ΚΟΙΝΩΝΙΚΩΝ ΜΕΣΩΝ", verbose_name="Service Title (EL)")
	service_description_en = models.TextField(default="When there's one great thing, there's usually another. What's your second thing to showcase?", verbose_name="Service Description (EN)")
	service_description_el = models.TextField(default="Όταν υπάρχει ένα υπέροχο πράγμα, συνήθως υπάρχει κι άλλο. Ποιο είναι το δεύτερό σας;", verbose_name="Service Description (EL)")
	service_button_text_en = models.CharField(max_length=100, default="VIEW INST ACC", verbose_name="Service Button (EN)")
	service_button_text_el = models.CharField(max_length=100, default="ΔΕΙΤΕ ΤΟ INST", verbose_name="Service Button (EL)")
	service_button_url = models.URLField(default="https://www.instagram.com/inadigiway", verbose_name="Service Button URL")
	service_image = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name="Service Image")
	
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Hero Section"
		verbose_name_plural = "Hero Section"

	def __str__(self):
		return "Hero Section Content"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class Service(models.Model):
	"""Individual service in the services section"""
	LAYOUT_CHOICES = [
		('left', 'Image Left, Content Right'),
		('right', 'Content Left, Image Right'),
	]
	
	title_en = models.CharField(max_length=200, verbose_name="Title (English)")
	title_el = models.CharField(max_length=200, verbose_name="Title (Greek)")
	description_en = models.TextField(verbose_name="Description (English)")
	description_el = models.TextField(verbose_name="Description (Greek)")
	image = models.ImageField(upload_to='services/', verbose_name="Service Image")
	layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='right', verbose_name="Layout")
	button_text_en = models.CharField(max_length=100, default="GET A QUOTE", verbose_name="Button Text (EN)")
	button_text_el = models.CharField(max_length=100, default="ΖΗΤΗΣΤΕ ΠΡΟΣΦΟΡΑ", verbose_name="Button Text (EL)")
	button_link = models.CharField(max_length=200, default="#quote", verbose_name="Button Link")
	sort_order = models.PositiveIntegerField(default=0, verbose_name="Sort Order")
	is_active = models.BooleanField(default=True, verbose_name="Active")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('sort_order', '-created_at')
		verbose_name = "Service"
		verbose_name_plural = "Services"

	def __str__(self):
		return self.title_en


class ServicesContent(models.Model):
	"""Services section general content - singleton model"""
	mega_text_en = models.CharField(max_length=200, default="IDEAS THAT CONVERT!", verbose_name="Mega Text (EN)")
	mega_text_el = models.CharField(max_length=200, default="ΙΔΕΕΣ ΠΟΥ ΜΕΤΑΤΡΕΠΟΝΤΑΙ!", verbose_name="Mega Text (EL)")
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Services Section Settings"
		verbose_name_plural = "Services Section Settings"

	def __str__(self):
		return "Services Section Settings"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class AboutContent(models.Model):
	"""About section content - singleton model"""
	title_en = models.CharField(max_length=200, default="Who's behind the Digi?", verbose_name="Title (EN)")
	title_el = models.CharField(max_length=200, default="Ποιος κρύβεται πίσω από το Digi;", verbose_name="Title (EL)")
	
	intro_name_en = models.CharField(max_length=200, default="Ina Lasko - a digital creative,", verbose_name="Intro Name (EN)")
	intro_name_el = models.CharField(max_length=200, default="Η Ίνα Λάσκο - μια ψηφιακή δημιουργός,", verbose_name="Intro Name (EL)")
	intro_text_en = models.CharField(max_length=300, default="based in Athens with a passion for brands that want to stand out!", verbose_name="Intro Text (EN)")
	intro_text_el = models.CharField(max_length=300, default="που εδρεύει στην Αθήνα με πάθος για brands που θέλουν να ξεχωρίσουν!", verbose_name="Intro Text (EL)")
	
	description_part1_en = models.CharField(max_length=100, default="Through", verbose_name="Description Part 1 (EN)")
	description_part1_el = models.CharField(max_length=100, default="Μέσα από το", verbose_name="Description Part 1 (EL)")
	brand_name_en = models.CharField(max_length=100, default="In A Digi Way,", verbose_name="Brand Name (EN)")
	brand_name_el = models.CharField(max_length=100, default="In A Digi Way,", verbose_name="Brand Name (EL)")
	description_part2_en = models.TextField(default="she combines strategic marketing with refined aesthetics, to give your social media, email campaigns and content a touch of... digital magic!", verbose_name="Description Part 2 (EN)")
	description_part2_el = models.TextField(default="συνδυάζει το στρατηγικό μάρκετινγκ με εκλεπτυσμένη αισθητική, για να δώσει στα social media, τις email καμπάνιες και το περιεχόμενό σας μια πινελιά... ψηφιακής μαγείας!", verbose_name="Description Part 2 (EL)")
	
	button_text_en = models.CharField(max_length=100, default="BOOK A CALL TODAY", verbose_name="Button Text (EN)")
	button_text_el = models.CharField(max_length=100, default="ΚΛΕΙΣΕ ΡΑΝΤΕΒΟΥ ΣΗΜΕΡΑ", verbose_name="Button Text (EL)")
	button_link = models.CharField(max_length=200, default="#book-call", verbose_name="Button Link")
	
	main_image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Main Image")
	badge_top_left = models.ImageField(upload_to='about/badges/', blank=True, null=True, verbose_name="Badge Top Left")
	badge_bottom_left = models.ImageField(upload_to='about/badges/', blank=True, null=True, verbose_name="Badge Bottom Left")
	badge_bottom_right = models.ImageField(upload_to='about/badges/', blank=True, null=True, verbose_name="Badge Bottom Right")
	
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "About Section"
		verbose_name_plural = "About Section"

	def __str__(self):
		return "About Section Content"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class ContactContent(models.Model):
	"""Contact section content - singleton model"""
	title_en = models.CharField(max_length=200, default="CONTACT FORM", verbose_name="Title (EN)")
	title_el = models.CharField(max_length=200, default="ΦΟΡΜΑ ΕΠΙΚΟΙΝΩΝΙΑΣ", verbose_name="Title (EL)")
	
	happy_clients_title_en = models.CharField(max_length=200, default="HAPPY CLIENTS", verbose_name="Happy Clients Title (EN)")
	happy_clients_title_el = models.CharField(max_length=200, default="ΕΥΧΑΡΙΣΤΗΜΕΝΟΙ ΠΕΛΑΤΕΣ", verbose_name="Happy Clients Title (EL)")
	
	# Form labels
	label_name_en = models.CharField(max_length=100, default="Name", verbose_name="Label: Name (EN)")
	label_name_el = models.CharField(max_length=100, default="Όνομα", verbose_name="Label: Name (EL)")
	label_phone_en = models.CharField(max_length=100, default="Phone", verbose_name="Label: Phone (EN)")
	label_phone_el = models.CharField(max_length=100, default="Τηλέφωνο", verbose_name="Label: Phone (EL)")
	label_email_en = models.CharField(max_length=100, default="E-mail", verbose_name="Label: Email (EN)")
	label_email_el = models.CharField(max_length=100, default="E-mail", verbose_name="Label: Email (EL)")
	label_service_en = models.CharField(max_length=100, default="Service", verbose_name="Label: Service (EN)")
	label_service_el = models.CharField(max_length=100, default="Υπηρεσία", verbose_name="Label: Service (EL)")
	label_budget_en = models.CharField(max_length=100, default="Budget", verbose_name="Label: Budget (EN)")
	label_budget_el = models.CharField(max_length=100, default="Προϋπολογισμός", verbose_name="Label: Budget (EL)")
	label_message_en = models.CharField(max_length=100, default="Message", verbose_name="Label: Message (EN)")
	label_message_el = models.CharField(max_length=100, default="Μήνυμα", verbose_name="Label: Message (EL)")
	
	button_submit_en = models.CharField(max_length=100, default="SUBMIT", verbose_name="Submit Button (EN)")
	button_submit_el = models.CharField(max_length=100, default="ΥΠΟΒΟΛΗ", verbose_name="Submit Button (EL)")
	
	# Service options
	service_select_en = models.CharField(max_length=100, default="Select a service", verbose_name="Select Service (EN)")
	service_select_el = models.CharField(max_length=100, default="Επιλέξτε υπηρεσία", verbose_name="Select Service (EL)")
	budget_select_en = models.CharField(max_length=100, default="Select budget", verbose_name="Select Budget (EN)")
	budget_select_el = models.CharField(max_length=100, default="Επιλέξτε προϋπολογισμό", verbose_name="Select Budget (EL)")
	
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Contact Section"
		verbose_name_plural = "Contact Section"

	def __str__(self):
		return "Contact Section Content"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class HappyClientsContent(models.Model):
	"""Happy Clients section content - singleton model"""
	title_en = models.CharField(max_length=200, default="HAPPY CLIENTS", verbose_name="Title (EN)")
	title_el = models.CharField(max_length=200, default="ΕΥΧΑΡΙΣΤΗΜΕΝΟΙ ΠΕΛΑΤΕΣ", verbose_name="Title (EL)")
	placeholder_text_en = models.CharField(max_length=200, default="Client testimonials coming soon...", verbose_name="Placeholder Text (EN)")
	placeholder_text_el = models.CharField(max_length=200, default="Οι μαρτυρίες πελατών έρχονται σύντομα...", verbose_name="Placeholder Text (EL)")
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Happy Clients Section"
		verbose_name_plural = "Happy Clients Section"

	def __str__(self):
		return "Happy Clients Section Content"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class FooterContent(models.Model):
	"""Footer section content - singleton model"""
	# Logo
	logo_image = models.ImageField(upload_to='footer/', blank=True, null=True, verbose_name="Footer Logo")
	
	# Social Media Links
	instagram_url = models.URLField(default="https://www.instagram.com/inadigiway", verbose_name="Instagram URL")
	facebook_url = models.URLField(default="https://www.facebook.com/61575931331769", verbose_name="Facebook URL")
	linkedin_url = models.URLField(default="https://linkedin.com", verbose_name="LinkedIn URL")
	
	# Contact Info
	phone_label_en = models.CharField(max_length=10, default="P.", verbose_name="Phone Label (EN)")
	phone_label_el = models.CharField(max_length=10, default="Τ.", verbose_name="Phone Label (EL)")
	phone_number = models.CharField(max_length=50, default="+30 697 1907 299", verbose_name="Phone Number")
	
	email_label_en = models.CharField(max_length=10, default="E.", verbose_name="Email Label (EN)")
	email_label_el = models.CharField(max_length=10, default="E.", verbose_name="Email Label (EL)")
	email_address = models.EmailField(default="info@inadigiway.com", verbose_name="Email Address")
	
	# QR Code
	qr_code_image = models.ImageField(upload_to='footer/', blank=True, null=True, verbose_name="QR Code")
	
	# Copyright
	copyright_text_en = models.CharField(max_length=200, default="In A Digi Way. All rights reserved.", verbose_name="Copyright (EN)")
	copyright_text_el = models.CharField(max_length=200, default="In A Digi Way. Με την επιφύλαξη κάθε δικαιώματος.", verbose_name="Copyright (EL)")
	copyright_year = models.PositiveIntegerField(default=2026, verbose_name="Copyright Year")
	
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Footer Section"
		verbose_name_plural = "Footer Section"

	def __str__(self):
		return "Footer Section Content"

	@classmethod
	def get_solo(cls):
		obj = cls.objects.order_by("-updated_at", "-id").first()
		if obj is None:
			obj = cls.objects.create()
		return obj


class ClientLogo(models.Model):
	"""Client logo for display in contact section"""
	name = models.CharField(max_length=100, verbose_name="Client Name")
	logo = models.ImageField(upload_to='client-logos/', verbose_name="Logo Image")
	sort_order = models.PositiveIntegerField(default=0, verbose_name="Sort Order")
	is_active = models.BooleanField(default=True, verbose_name="Active")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['sort_order', 'name']
		verbose_name = "Client Logo"
		verbose_name_plural = "Client Logos"

	def __str__(self):
		return self.name
