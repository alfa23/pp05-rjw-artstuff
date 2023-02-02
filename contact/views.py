from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact, Newletter
from .forms import ContactForm, NewsletterForm


def contact(request):
    """ View to contact page """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been received.')
            return redirect('contact_success')
        else:
            messages.error(request, 'Failed to submit message \
                Please ensure the form is valid')
    else:
        contact_form = ContactForm()
    newsletter_form = NewsletterForm()
    context = {
        'contact': contact_form,
        'newsletter': newsletter_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """ View to contact success page """
    newsletter_form = NewsletterForm()
    context = {
        'newsletter': newsletter_form,
    }

    return render(request, 'contact/contact_success.html', context)


def newsletter_sub(request):
    """ View to handle newsletter subscription """
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'You have been subscribed!')
        else:
            messages.error(request, 'Failed to subscribe \
                Please ensure the form is valid')
    return redirect('contact')
