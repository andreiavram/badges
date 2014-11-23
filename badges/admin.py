from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import ModelAdmin
from badges.models import Badge, Eveniment


class EvenimentAdmin(ModelAdmin):
    list_display = ["nume", "an"]
    list_filter = ["an"]


class BadgeAdmin(ModelAdmin):
    list_display = ['eveniment_nume', 'eveniment_an', 'poster', 'imagine']
    list_filter = ["poster"]

    def eveniment_nume(self, obj):
        return obj.eveniment.nume

    def eveniment_an(self, obj):
        return obj.eveniment.an

admin.site.register(Badge, BadgeAdmin)
admin.site.register(Eveniment, EvenimentAdmin)