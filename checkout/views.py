from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': (
            'pk_test_51MEYOzD6HdanpD9ScXXgbUl9zHeLD2nWpC9GNw'
            'XbsuVN0a718pN8xBAMXqVZkkBTW0eVaiDVm25A2AYO6MIR0Zva00bP9HhLUF'
        ),
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
