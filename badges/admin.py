from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import ModelAdmin
from badges.models import Badge


class BadgeAdmin(ModelAdmin):
    list_display = ['nume_activitate', 'an_activitate', 'poster']
    list_filter = ['an_activitate']


admin.site.register(Badge, BadgeAdmin)