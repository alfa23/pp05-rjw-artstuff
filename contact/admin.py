from django.contrib import admin
from .models import Contact, Newletter


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


class NewletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )


admin.site.register(Newletter, NewletterAdmin)
