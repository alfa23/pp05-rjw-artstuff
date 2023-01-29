from django.db import models


class Contact(models.Model):
    """ A model for the customer contact form """

    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=600, null=False, blank=False)
    mobile = models.CharField(max_length=25, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Newletter(models.Model):
    """ A model for the customer newsletter subscription form """

    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
