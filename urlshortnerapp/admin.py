from django.contrib import admin
from .models import URLMapping

# Register your models here.

class SettingURLMapping(admin.ModelAdmin):
    list_display = ('long_url','short_code')

admin.site.register(URLMapping,SettingURLMapping)
