from django import forms
from .models import QuoteRequest


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name", "email", "phone", "service", "budget", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"required": True, "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"required": True, "placeholder": "your@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+30 69..."}),
            "service": forms.TextInput(attrs={"placeholder": "Service you're interested in"}),
            "budget": forms.TextInput(attrs={"placeholder": "Estimated budget"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us about your project..."}),
        }
