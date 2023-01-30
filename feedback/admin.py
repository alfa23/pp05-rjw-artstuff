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

    list_filter = (
        'author',
        'user_rating',
        'product',
    )

    ordering = ('-created_on',)


admin.site.register(Feedback, FeedbackAdmin)
