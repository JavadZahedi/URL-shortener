from django.contrib import admin
from .models import URL

# Register your models here.

class URLAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created_jalali', 'last_visit_jalali', 'author')

admin.site.register(URL, URLAdmin)
