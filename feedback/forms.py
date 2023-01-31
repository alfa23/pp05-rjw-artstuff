from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('title', 'body', 'user_rating')
        widgets = {
            'user_rating': forms.NumberInput(attrs={
                'max': '5',  # Sets maximum value
                'min': '0',  # Sets minimum value
            })
        }
