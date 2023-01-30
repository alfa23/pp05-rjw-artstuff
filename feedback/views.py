from django.shortcuts import render
from products.models import Product
from .models import Feedback


def view_feedback(request):
    """ View to show user's feedback entries """
    # feedback = Feedback.objects.filter(author=request.user)
    # template = 'feedback/view_feedback.html'

    return render(request, 'feedback/view_feedback.html')
