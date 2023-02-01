from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'subject',
        'created_on',
    )

    ordering = ('-created_on',)


admin.site.register(Contact, ContactAdmin)
