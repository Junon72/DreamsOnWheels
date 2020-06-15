from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm

def contact(request):
    contact_request = ContactForm

    if request.method == 'POST':
        contact_form = contact_request(request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            from_email = request.POST.get('from_email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            template = get_template('message_template.txt')
            context = {
                'name': name,
                'from_email': from_email,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New message",
                content,
                "DOW" +'',
                ['admin@dow.com'],
                reply_to=[from_email]
            )
            email.send()

            messages.success(request, "Your message was sent successfully!")
            return redirect('contact:contact')
        else:
            messages.error(request, "Your message was not sent. Please try again.")
            return redirect(reverse('contact'))
    context = {
        'title': 'Contact',
        'contact_form': contact_request
    }
    return render(request, "contact.html", context)
