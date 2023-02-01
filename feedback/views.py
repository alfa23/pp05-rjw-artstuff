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
    # feedback = get_object_or_404(Feedback, pk=feedback_id)

    template = 'feedback/view_feedback.html'

    context = {
        'feedbacks': feedbacks,
        # 'feedback': feedback,
    }

    return render(request, template, context)


@login_required
def add_feedback(request, product_id):
    """ Display form to add feedback to a product """
    product = get_object_or_404(Product, pk=product_id)
    feedbacks = Feedback.objects.filter(author=request.user)
    user_feedback = Feedback.objects.filter(
        author=request.user, product=product)

    # Check if user already submitted feedback for the product
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

                # update_product_rating(product)

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to submit feedback. \
                    Please ensure the form is valid.')
        else:
            form = FeedbackForm()

    template = 'feedback/add_feedback.html'

    context = {
        'product': product,
        'feedbacks': feedbacks,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_feedback(request, feedback_id):
    """ Display form to allow users to edit their feedback """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    feedbacks = (
        Feedback.objects.filter(author=request.user).exclude(pk=feedback_id)
    )

    if request.user != feedback.author:
        messages.error(
            request, 'You are not authorised to edit this feedback.'
        )
        return redirect(reverse('view_feedback'))

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your feedback!')

            # update_product_rating(feedback.product)

            return redirect('view_feedback')
        else:
            messages.error(request, 'Failed to update your feedback. \
                Please ensure the form is valid.')
    else:
        form = FeedbackForm(instance=feedback)
        messages.info(request, f'You are editing your feedback for \
            {feedback.product.name}')

    template = 'feedback/edit_feedback.html'

    context = {
        'form': form,
        'feedback': feedback,
        'feedbacks': feedbacks,
    }

    return render(request, template, context)


@login_required
def delete_feedback(request, feedback_id):
    """ Delete an existing feedback item """
    feedback = get_object_or_404(Feedback, pk=feedback_id)

    if request.user != feedback.author:
        messages.error(request, 'You are not authorised \
            to delete this feedback.')
        return redirect(reverse('view_feedback'))

    feedback.delete()
    messages.success(request, 'Your feedback has been deleted!')
    # print('feedback', feedback)
    # update_product_rating(feedback.product)

    return redirect(reverse('view_feedback'))


# def update_product_rating(product):
#     """ Update the rating field for the product """

#     total_feedbacks = feedback.objects.filter(product=product)
#     nr_of_total_feedbacks = total_feedbacks.count()
#     ratings_sum = 0

#     if nr_of_total_feedbacks <= 0:
#         product.rating = None
#     else:
#         for feedback in total_feedbacks:
#             ratings_sum += feedback.user_rating

#         # calculate raw_rating average & round to 1dp:
#         raw_rating = ratings_sum / nr_of_total_feedbacks
#         rounded_rating = round(raw_rating, 1)

#         product.rating = rounded_rating

#     product.save()
