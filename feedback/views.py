from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Feedback
from .forms import FeedbackForm


@login_required
def view_feedback(request):
    """ View to show user's feedback entries """
    feedbacks = Feedback.objects.filter(author=request.user)

    template = 'feedback/view_feedback.html'

    context = {
        'feedbacks': feedbacks,
    }

    return render(request, template, context)


@login_required
def add_feedback(request, product_id):
    """ Display form to add feedback to a product """
    product = get_object_or_404(Product, pk=product_id)
    user_feedback = Feedback.objects.filter(
        author=request.user, product=product)

    # Check if user already submitted a review for the product
    if user_feedback:
        messages.error(request,
                       'You have already submitted feedback for this product')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        if request.method == 'POST':
            form = FeedbackForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.product = product
                form.save()
                messages.success(request,
                                 'Your product feedback has been submitted')

                update_product_rating(product)

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to submit feedback. \
                    Please ensure the form is valid.')
        else:
            form = FeedbackForm()

    template = 'feedback/add_feedback.html'

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


def update_product_rating(product):
    """ Update the rating field for the product """

    total_feedbacks = feedback.objects.filter(product=product)
    nr_of_total_feedbacks = total_feedbacks.count()
    ratings_sum = 0

    if nr_of_total_feedbacks <= 0:
        product.rating = None
    else:
        for feedback in total_feedbacks:
            ratings_sum += feedback.user_rating

        # calculate raw_rating average & round to 1dp:
        raw_rating = ratings_sum / nr_of_total_feedbacks
        rounded_rating = round(raw_rating, 1)

        product.rating = rounded_rating

    product.save()
