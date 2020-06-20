from django.core.mail import EmailMessage
from django.template.loader import get_template, render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm


def contact(request):
    contact_request = ContactForm

    if request.method == 'POST':
        form = contact_request(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            template = get_template('message_template.txt')
            context = {
                'name': name,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                from_email,
                ['adminDOW@dow.com'],
                headers = {'Reply-To': from_email}
            )
            email.send()
            form.save()

            messages.success(
                request,
                "Thank you for contacting us! We will get back to you in short."
            )
            return redirect('contact:contact')
        else:
            messages.error(
                request,
                "Your message was not sent. Please try again."
            )
            return redirect(reverse('contact'))
    context = {
        'title': 'Contact',
        'contact_form': contact_request
    }
    return render(request, "contact.html", context)
