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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'body': 'Your feedback',
            'user_rating': 'Your rating (0-5)',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-accent \
                rounded-0 feedback-form-input'
            self.fields[field].label = False
