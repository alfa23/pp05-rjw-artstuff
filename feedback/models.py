from django.db import models
from django.contrib.auth.models import User
from products.models import Product

from django.db.models import CheckConstraint, Q, UniqueConstraint


class Feedback(models.Model):
    """ Model for user feedback """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='feedback'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_feedback'
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user_rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        ordering = ['-created_on']
        constraints = [
            CheckConstraint(
                check=Q(user_rating__range=(0, 5)), name='valid_user_rating'
            ),
            UniqueConstraint(fields=['author', 'product'], name='rating_once')
        ]

    def __str__(self):
        return f'{self.product} feedback from {self.author}'
