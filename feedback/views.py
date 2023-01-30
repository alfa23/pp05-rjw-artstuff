from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Feedback


@login_required
def view_feedback(request):
    """ View to show user's feedback entries """
    feedbacks = Feedback.objects.filter(author=request.user)

    template = 'feedback/view_feedback.html'

    context = {
        'feedbacks': feedbacks,
    }

    return render(request, template, context)
