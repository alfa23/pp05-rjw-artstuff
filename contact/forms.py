from django import forms
from .models import Contact, Newletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newletter
        fields = ['email', ]
