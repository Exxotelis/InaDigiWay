from django.urls import path
from .views import home, contact_submit

urlpatterns = [
    path('', home, name='home'),
    path('contact/submit/', contact_submit, name='contact_submit'),
]
