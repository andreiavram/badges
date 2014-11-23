from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import ModelAdmin
from users.models import Utilizator

class UserAdmin(ModelAdmin):
    list_display = ["username", "first_name", "last_name"]

    def username(self, obj):
        return obj.user.username

admin.site.register(Utilizator, UserAdmin)