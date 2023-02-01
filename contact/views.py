from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ View to contact page """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message received!')
            return redirect('contact_success')
        else:
            messages.error(request, 'Failed to submit message \
                Please ensure the form is valid')
    else:
        contact_form = ContactForm()

    context = {
        'contact': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """ View to contact success page """
    # contact_form = ContactForm()

    context = {
        # 'contact': contact_form,
    }

    return render(request, 'contact/contact_success.html', context)
