from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """ View to contact page """
    contact_form = ContactForm()

    context = {
        'contact': contact_form,
    }

    return render(request, 'contact/contact.html', context)
