from django.urls import path
from .views import contact_submit, quote_submit

urlpatterns = [
    path('contact/submit/', contact_submit, name='contact_submit'),
    path('quote/submit/', quote_submit, name='quote_submit'),
]
