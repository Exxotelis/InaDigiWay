from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission"""
    try:
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        budget = request.POST.get('budget', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, message]):
            return JsonResponse({
                'status': 'error',
                'message': 'Please fill in all required fields (Name, Email, Message)'
            }, status=400)
        
        # Prepare email
        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"""
        New Contact Form Submission
        
        Name: {name}
        Phone: {phone or 'Not provided'}
        Email: {email}
        Service: {service or 'Not specified'}
        Budget: {budget or 'Not specified'}
        
        Message:
        {message}
        """
        
        # Send email
        try:
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            # Optionally send confirmation email to user
            send_mail(
                "We received your message",
                f"Hi {name},\n\nThank you for contacting us. We'll get back to you soon!\n\nBest regards,\nIna Digi Way",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email error: {e}")
            # Continue anyway - don't let email errors break the submission
        
        return JsonResponse({
            'status': 'success',
            'message': 'Thank you for your message! We will get back to you soon.'
        })
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }, status=500)
