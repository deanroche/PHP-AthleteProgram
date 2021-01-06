from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_date',
                    'contact_title', 'read_status',)
    list_display_links = ('contact_name', 'contact_email', 'contact_date',
                          'contact_title', 'read_status')
    search_fields = ('contact_name', 'contact_email', 'read_status',)
    list_filter = ('read_status', 'contact_date',)
    list_per_page = 15


# Register your models here.
admin.site.register(Contact, ContactAdmin)
