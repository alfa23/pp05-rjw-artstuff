from django.shortcuts import render


def contact(request):
    """ View to contact page """

    return render(request, 'contact/contact.html')
