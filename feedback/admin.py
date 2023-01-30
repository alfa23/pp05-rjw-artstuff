from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'product',
        'created_on',
        'user_rating',
    )

    ordering = ('-created_on',)


admin.site.register(Feedback, FeedbackAdmin)
